from __future__ import annotations

import ctypes
import errno
import fcntl
import os
import v4l2.uapi

__all__ = [ 'Route', 'SubDevice' ]

class Route:
    def __init__(self) -> None:
        self.sink_pad = 0
        self.sink_stream = 0
        self.source_pad = 0
        self.source_stream = 0
        self.flags = 0

    @property
    def is_active(self):
        return (self.flags & v4l2.uapi.V4L2_SUBDEV_ROUTE_FL_ACTIVE) != 0

    def __repr__(self) -> str:
        return f'Route({self.sink_pad}/{self.sink_stream}->{self.source_pad}/{self.source_stream} ({self.flags:#x}))'

    @classmethod
    def from_v4l2_subdev_route(cls, route: v4l2.uapi.v4l2_subdev_route):
        r = Route()
        r.sink_pad = route.sink_pad
        r.sink_stream = route.sink_stream
        r.source_pad = route.source_pad
        r.source_stream = route.source_stream
        r.flags = route.flags
        return r

    def to_v4l2_subdev_route(self):
        r = v4l2.uapi.v4l2_subdev_route(sink_pad=self.sink_pad,
                                   sink_stream=self.sink_stream,
                                   source_pad=self.source_pad,
                                   source_stream=self.source_stream,
                                   flags=self.flags)
        return r


class SubDevice:
    def __init__(self, entity: v4l2.MediaEntity) -> None:
        self.entity = entity
        assert(entity.interface.is_subdev)
        self.fd = os.open(entity.interface.dev_path, os.O_RDWR | os.O_NONBLOCK)
        assert(self.fd != -1)

        try:
            cap = v4l2.uapi.v4l2_subdev_client_capability()
            cap.capabilities = v4l2.uapi.V4L2_SUBDEV_CLIENT_CAP_STREAMS
            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_CLIENT_CAP, cap, True)
            self.has_streams = (cap.capabilities & v4l2.uapi.V4L2_SUBDEV_CLIENT_CAP_STREAMS) != 0
        except:
            self.has_streams = False

    def get_format(self, pad, stream=0, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE):
        fmt = v4l2.uapi.v4l2_subdev_format()
        fmt.pad = pad
        fmt.stream = stream
        fmt.which = which
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_FMT, fmt, True)
        return fmt

    def set_format(self, pad, stream, w, h, code, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE):
        fmt = self.get_format(pad, stream, which)

        #fmt = v4l2.uapi.v4l2_subdev_format()
        fmt.pad = pad
        fmt.stream = stream
        fmt.which = which
        fmt.format.width = w
        fmt.format.height = h
        fmt.format.code = code
        fmt.format.field = v4l2.uapi.V4L2_FIELD_NONE
        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_FMT, fmt, True)

    def get_routes(self, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE) -> list[Route]:
        routing = v4l2.uapi.v4l2_subdev_routing()
        routing.which = which

        try:
            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_ROUTING, routing, True)
        except OSError as e:
            if e.errno == errno.ENOTTY:
                return []
            elif e.errno != errno.ENOSPC:
                raise

        routes = (v4l2.uapi.v4l2_subdev_route * routing.num_routes)()
        routing.routes = ctypes.addressof(routes)

        try:
            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_ROUTING, routing, True)
        except OSError as e:
            if e.errno == errno.ENOTTY:
                routes = (v4l2.uapi.v4l2_subdev_route * 0)()
            else:
                raise

        routes = [Route.from_v4l2_subdev_route(r) for r in routes]

        return routes

    def set_routes(self, routes: list[Route], which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE) -> list[Route]:
        # Allocate extra space for return routes
        kroutes = (v4l2.uapi.v4l2_subdev_route * 16)()
        for i,route in enumerate(routes):
            kroutes[i] = route.to_v4l2_subdev_route()

        routing = v4l2.uapi.v4l2_subdev_routing()
        routing.which = which
        routing.len_routes = len(kroutes)
        routing.num_routes = len(routes)
        routing.routes = ctypes.addressof(kroutes)

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_ROUTING, routing, True)

        routes = [Route.from_v4l2_subdev_route(kroutes[idx]) for idx in range(routing.num_routes)]

        return routes

    def get_selection(self, target, pad, stream=0, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE):
        sel = v4l2.uapi.v4l2_subdev_selection()
        sel.pad = pad
        sel.stream = stream
        sel.which = which
        sel.target = target
        sel.flags = 0

        try:
            fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_G_SELECTION, sel, True)
        except OSError as e:
            if e.errno == errno.ENOTTY:
                return v4l2.uapi.v4l2_rect()

        return sel.r

    def set_selection(self, target, rect: v4l2.uapi.v4l2_rect, pad, stream=0, which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE):
        sel = v4l2.uapi.v4l2_subdev_selection()
        sel.pad = pad
        sel.stream = stream
        sel.which = which
        sel.target = target
        sel.flags = 0
        sel.r = rect

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_SELECTION, sel, True)

        return sel.r

    def set_frame_interval(self, pad, stream, interval: tuple[int, int], which=v4l2.uapi.V4L2_SUBDEV_FORMAT_ACTIVE):
        v4l2_ival = v4l2.uapi.v4l2_subdev_frame_interval()
        v4l2_ival.pad = pad
        v4l2_ival.stream = stream
        v4l2_ival.which = which
        v4l2_ival.interval = interval

        fcntl.ioctl(self.fd, v4l2.uapi.VIDIOC_SUBDEV_S_FRAME_INTERVAL, v4l2_ival, True)

        return (v4l2_ival.interval.numerator, v4l2_ival.interval.denominator)
