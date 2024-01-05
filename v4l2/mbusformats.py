from __future__ import annotations

from enum import IntEnum

import v4l2.uapi

# str.join('\n', [f'    {e[14:]} = v4l2.uapi.{e}' for e in v4l2.uapi.__dir__() if e.startswith("V4L2_MBUS_FMT_")])

class BusFormat(IntEnum):
    FIXED = v4l2.uapi.V4L2_MBUS_FMT_FIXED
    RGB444_2X8_PADHI_BE = v4l2.uapi.V4L2_MBUS_FMT_RGB444_2X8_PADHI_BE
    RGB444_2X8_PADHI_LE = v4l2.uapi.V4L2_MBUS_FMT_RGB444_2X8_PADHI_LE
    RGB555_2X8_PADHI_BE = v4l2.uapi.V4L2_MBUS_FMT_RGB555_2X8_PADHI_BE
    RGB555_2X8_PADHI_LE = v4l2.uapi.V4L2_MBUS_FMT_RGB555_2X8_PADHI_LE
    BGR565_2X8_BE = v4l2.uapi.V4L2_MBUS_FMT_BGR565_2X8_BE
    BGR565_2X8_LE = v4l2.uapi.V4L2_MBUS_FMT_BGR565_2X8_LE
    RGB565_2X8_BE = v4l2.uapi.V4L2_MBUS_FMT_RGB565_2X8_BE
    RGB565_2X8_LE = v4l2.uapi.V4L2_MBUS_FMT_RGB565_2X8_LE
    RGB666_1X18 = v4l2.uapi.V4L2_MBUS_FMT_RGB666_1X18
    RGB888_1X24 = v4l2.uapi.V4L2_MBUS_FMT_RGB888_1X24
    RGB888_2X12_BE = v4l2.uapi.V4L2_MBUS_FMT_RGB888_2X12_BE
    RGB888_2X12_LE = v4l2.uapi.V4L2_MBUS_FMT_RGB888_2X12_LE
    ARGB8888_1X32 = v4l2.uapi.V4L2_MBUS_FMT_ARGB8888_1X32
    Y8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_Y8_1X8
    UV8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_UV8_1X8
    UYVY8_1_5X8 = v4l2.uapi.V4L2_MBUS_FMT_UYVY8_1_5X8
    VYUY8_1_5X8 = v4l2.uapi.V4L2_MBUS_FMT_VYUY8_1_5X8
    YUYV8_1_5X8 = v4l2.uapi.V4L2_MBUS_FMT_YUYV8_1_5X8
    YVYU8_1_5X8 = v4l2.uapi.V4L2_MBUS_FMT_YVYU8_1_5X8
    UYVY8_2X8 = v4l2.uapi.V4L2_MBUS_FMT_UYVY8_2X8
    VYUY8_2X8 = v4l2.uapi.V4L2_MBUS_FMT_VYUY8_2X8
    YUYV8_2X8 = v4l2.uapi.V4L2_MBUS_FMT_YUYV8_2X8
    YVYU8_2X8 = v4l2.uapi.V4L2_MBUS_FMT_YVYU8_2X8
    Y10_1X10 = v4l2.uapi.V4L2_MBUS_FMT_Y10_1X10
    UYVY10_2X10 = v4l2.uapi.V4L2_MBUS_FMT_UYVY10_2X10
    VYUY10_2X10 = v4l2.uapi.V4L2_MBUS_FMT_VYUY10_2X10
    YUYV10_2X10 = v4l2.uapi.V4L2_MBUS_FMT_YUYV10_2X10
    YVYU10_2X10 = v4l2.uapi.V4L2_MBUS_FMT_YVYU10_2X10
    Y12_1X12 = v4l2.uapi.V4L2_MBUS_FMT_Y12_1X12
    UYVY8_1X16 = v4l2.uapi.V4L2_MBUS_FMT_UYVY8_1X16
    VYUY8_1X16 = v4l2.uapi.V4L2_MBUS_FMT_VYUY8_1X16
    YUYV8_1X16 = v4l2.uapi.V4L2_MBUS_FMT_YUYV8_1X16
    YVYU8_1X16 = v4l2.uapi.V4L2_MBUS_FMT_YVYU8_1X16
    YDYUYDYV8_1X16 = v4l2.uapi.V4L2_MBUS_FMT_YDYUYDYV8_1X16
    UYVY10_1X20 = v4l2.uapi.V4L2_MBUS_FMT_UYVY10_1X20
    VYUY10_1X20 = v4l2.uapi.V4L2_MBUS_FMT_VYUY10_1X20
    YUYV10_1X20 = v4l2.uapi.V4L2_MBUS_FMT_YUYV10_1X20
    YVYU10_1X20 = v4l2.uapi.V4L2_MBUS_FMT_YVYU10_1X20
    YUV10_1X30 = v4l2.uapi.V4L2_MBUS_FMT_YUV10_1X30
    AYUV8_1X32 = v4l2.uapi.V4L2_MBUS_FMT_AYUV8_1X32
    UYVY12_2X12 = v4l2.uapi.V4L2_MBUS_FMT_UYVY12_2X12
    VYUY12_2X12 = v4l2.uapi.V4L2_MBUS_FMT_VYUY12_2X12
    YUYV12_2X12 = v4l2.uapi.V4L2_MBUS_FMT_YUYV12_2X12
    YVYU12_2X12 = v4l2.uapi.V4L2_MBUS_FMT_YVYU12_2X12
    UYVY12_1X24 = v4l2.uapi.V4L2_MBUS_FMT_UYVY12_1X24
    VYUY12_1X24 = v4l2.uapi.V4L2_MBUS_FMT_VYUY12_1X24
    YUYV12_1X24 = v4l2.uapi.V4L2_MBUS_FMT_YUYV12_1X24
    YVYU12_1X24 = v4l2.uapi.V4L2_MBUS_FMT_YVYU12_1X24
    SBGGR8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SBGGR8_1X8
    SGBRG8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SGBRG8_1X8
    SGRBG8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SGRBG8_1X8
    SRGGB8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SRGGB8_1X8
    SBGGR10_ALAW8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SBGGR10_ALAW8_1X8
    SGBRG10_ALAW8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SGBRG10_ALAW8_1X8
    SGRBG10_ALAW8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SGRBG10_ALAW8_1X8
    SRGGB10_ALAW8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SRGGB10_ALAW8_1X8
    SBGGR10_DPCM8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SBGGR10_DPCM8_1X8
    SGBRG10_DPCM8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SGBRG10_DPCM8_1X8
    SGRBG10_DPCM8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SGRBG10_DPCM8_1X8
    SRGGB10_DPCM8_1X8 = v4l2.uapi.V4L2_MBUS_FMT_SRGGB10_DPCM8_1X8
    SBGGR10_2X8_PADHI_BE = v4l2.uapi.V4L2_MBUS_FMT_SBGGR10_2X8_PADHI_BE
    SBGGR10_2X8_PADHI_LE = v4l2.uapi.V4L2_MBUS_FMT_SBGGR10_2X8_PADHI_LE
    SBGGR10_2X8_PADLO_BE = v4l2.uapi.V4L2_MBUS_FMT_SBGGR10_2X8_PADLO_BE
    SBGGR10_2X8_PADLO_LE = v4l2.uapi.V4L2_MBUS_FMT_SBGGR10_2X8_PADLO_LE
    SBGGR10_1X10 = v4l2.uapi.V4L2_MBUS_FMT_SBGGR10_1X10
    SGBRG10_1X10 = v4l2.uapi.V4L2_MBUS_FMT_SGBRG10_1X10
    SGRBG10_1X10 = v4l2.uapi.V4L2_MBUS_FMT_SGRBG10_1X10
    SRGGB10_1X10 = v4l2.uapi.V4L2_MBUS_FMT_SRGGB10_1X10
    SBGGR12_1X12 = v4l2.uapi.V4L2_MBUS_FMT_SBGGR12_1X12
    SGBRG12_1X12 = v4l2.uapi.V4L2_MBUS_FMT_SGBRG12_1X12
    SGRBG12_1X12 = v4l2.uapi.V4L2_MBUS_FMT_SGRBG12_1X12
    SRGGB12_1X12 = v4l2.uapi.V4L2_MBUS_FMT_SRGGB12_1X12
    JPEG_1X8 = v4l2.uapi.V4L2_MBUS_FMT_JPEG_1X8
    S5C_UYVY_JPEG_1X8 = v4l2.uapi.V4L2_MBUS_FMT_S5C_UYVY_JPEG_1X8
    AHSV8888_1X32 = v4l2.uapi.V4L2_MBUS_FMT_AHSV8888_1X32

    # XXX Manually added entries
    META_8 = 0x8001
    META_10 = 0x8002
    META_12 = 0x8003

    SBGGR16_1X16 = 0x301d
    SGBRG16_1X16 = 0x301e
    SGRBG16_1X16 = 0x301f
    SRGGB16_1X16 = 0x3020

    # XXX deprecated rpi format
    SENSOR_DATA = 0x77002
