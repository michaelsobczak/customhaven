
from PIL import ImageFont, ImageDraw, Image
import os

_FONT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'assets', 'fonts', 'PirataOne-Gloomhaven.ttf')
_ABILITY_CARD_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'assets', 'images', 'ability.png')

def load_font(path: str = _FONT_PATH, size: int = 10):
    return ImageFont.truetype(_FONT_PATH, size=size)

def load_ability_card_background(width: int = 413, height: int = 563) -> Image:
    return Image.open(_ABILITY_CARD_PATH).resize((width, height))


def draw_text(text: str, x: int, y: int, image: Image, font):
    d = ImageDraw.Draw(image)
    d.text((x,y), text, font=font, fill=(255,255,255,255))

# def tint(image: Image, r: int, g: int, b: int, a: int):
#     tint = (r/255.0, g/255.0, b/255.0,a/255.0)
#     pix = im.load()
#     for x in xrange( im.size[0] ):
#     for y in xrange( im.size[1] ):
#     c = pix[x,y]
#     pix[x,y] = (int(c[0]*tint[0]), int(c[1]*tint[1]),
#     int(c[2]*tint[2]), c[3])


def _tint(img, color):
    color_map = []
    for component in color:
        color_map.extend(int(component/255.0*i) for i in range(256))
    return img.point(color_map)