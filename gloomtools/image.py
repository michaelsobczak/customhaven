
from PIL import ImageFont, ImageDraw, Image
import os

_FONT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'assets', 'fonts', 'PirataOne-Gloomhaven.ttf')
_ABILITY_CARD_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'assets', 'images', 'ability.png')

_CARD_TITLE_X = 120
_CARD_TITLE_Y = 10
_CARD_TITLE_SIZE = 40

_CARD_INITIATIVE_X = 196
_CARD_INITIATIVE_Y = 278
_CARD_INITIATIVE_SIZE = 30

def load_font(path: str = _FONT_PATH, size: int = 10):
    return ImageFont.truetype(_FONT_PATH, size=size)


def load_ability_card_background(width: int = 413, height: int = 563) -> Image:
    return Image.open(_ABILITY_CARD_PATH).resize((width, height))


def draw_text(text: str, x: int, y: int, image: Image, font):
    d = ImageDraw.Draw(image)
    d.text((x,y), text, font=font, fill=(255,255,255,255))


def tint(img: Image, r: int, g: int, b: int, a: int = 255):
    color = (r, g, b, a)
    color_map = []
    for component in color:
        color_map.extend(int(component/255.0*i) for i in range(256))
    return img.point(color_map)


def draw_ability_card(title: str, initiative: int, toptext: str, bottomtext: str, color):

    card = load_ability_card_background()
    card = tint(card, *color)
    font = load_font(size=_CARD_TITLE_SIZE)
    draw_text(text=title, x=_CARD_TITLE_X, y=_CARD_TITLE_Y, image=card, font=font)

    initiative_font = load_font(size=_CARD_INITIATIVE_SIZE)
    draw_text(text=str(initiative), x=_CARD_INITIATIVE_X, y=_CARD_INITIATIVE_Y, image=card, font=initiative_font)
    return card
