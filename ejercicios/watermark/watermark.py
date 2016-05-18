# Based on https://gist.github.com/snay2/876425

import glob
import os
from PIL import Image, ImageDraw, ImageFont

def main(origins='pics/*', destination='wpics'):
    for i in glob.glob(origins):
        watermark(i, destination)


def watermark(image_file, destination):
    image = Image.open(image_file)
    watermark = Image.new("RGBA", image.size)
    waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")

    waterdraw.text((10, 10), "juanjoconti.com", font=ImageFont.truetype("open-sans/OpenSans-Bold.ttf", 38))

    watermask = watermark.convert("L").point(lambda x: min(x, 100))

    watermark.putalpha(watermask)

    image.paste(watermark, None, watermark)
    image.save(os.path.join(destination, os.path.basename(image_file)), "JPEG")


if __name__ == '__main__':
    main()