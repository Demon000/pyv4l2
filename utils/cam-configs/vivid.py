import v4l2

imx219_w = 640
imx219_h = 480
imx219_bus_fmt = v4l2.BusFormat.SBGGR8_1X8
imx219_pix_fmt = v4l2.PixelFormats.SBGGR8

mbus_fmt_imx219 = (imx219_w, imx219_h, imx219_bus_fmt)
fmt_pix_imx219 = (imx219_w, imx219_h, imx219_pix_fmt)

configurations = {}

configurations['cam0'] = {
    'media': ('vivid', 'model'),

    'devices': [
        {
            'entity': 'vivid-000-vid-cap',
            'fmt': fmt_pix_imx219,
        },
    ],
}

def get_configs(**kwargs):
    return (configurations, ['cam0'])
