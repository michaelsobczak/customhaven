
from PIL import ImageFont, ImageDraw, Image
from typing import List, Tuple
import os

_ICON_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'assets', 'icons')
_FONT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'assets', 'fonts', 'PirataOne-Gloomhaven.ttf')
_ABILITY_CARD_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'assets', 'images', 'ability.png')

_CARD_TITLE_X = 120
_CARD_TITLE_Y = 10
_CARD_TITLE_SIZE = 40

_CARD_INITIATIVE_X = 196
_CARD_INITIATIVE_Y = 278
_CARD_INITIATIVE_SIZE = 30

_CARD_TEXT_SIZE = 15

_CARD_TOP_TEXT_X = 60
_CARD_TOP_TEXT_Y = 110

_CARD_BOTTOM_TEXT_X = 60
_CARD_BOTTOM_TEXT_Y = 358

_CARD_ICON_WIDTH = 30
_CARD_ICON_HEIGHT = 30

_CARD_TEXT_WIDTH = 5
_CARD_ICON_PADDING_X = 1.05
_CARD_ICON_PADDING_Y = 1.10

_CARD_LEVEL_X = 204
_CARD_LEVEL_Y = 68

_CARD_LOSS_X = 300
_CARD_LOSS_TOP_Y = 250
_CARD_LOSS_BOTTOM_Y = 450

def load_icon(name: str) -> Image:
    name = name.lower()
    for iconfile in os.listdir(_ICON_DIR):
        bname, ext = os.path.splitext(iconfile)
        if bname.lower() == name and ext.replace('.', '') in ['jpeg', 'jpg', 'png']:
            return Image.open(os.path.join(_ICON_DIR, iconfile))
    print(f'Unable to find {name}')
    return None


def draw_icon(img, icon,  x, y, w=_CARD_ICON_WIDTH, h=_CARD_ICON_HEIGHT):
    ic = load_icon(icon).resize((w, h))
    img.paste(ic, (x, y))


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


def draw_ability_line(image: Image, text: str, x: int, y: int):
    pending_text = ''
    current_x = x
    text_font = load_font(size=_CARD_TEXT_SIZE)
    for token in text.split(' '):
        if '{' in token:
            if pending_text:
                draw_text(pending_text, current_x, y, image, text_font)
                current_x += (_CARD_TEXT_WIDTH * len(pending_text))
                pending_text = ''
            icons = [ i for i in token.replace('{', '').replace('}', '').split(':') if i ]
            [ draw_icon(image, icon, current_x, y) for icon in icons ]
            current_x += int(_CARD_ICON_WIDTH * 1.05)
        else:
            pending_text += f'{token} '

    if pending_text:
        draw_text(pending_text, current_x, y, image, text_font)


def draw_ability_card(title: str, initiative: int, toplines: List[str], bottomlines: List[str],
                      color: Tuple[int,int,int], level: str, toploss: bool, bottomloss: bool,
                      topduration: str, topaoe: str, topquest: str,
                      bottomduration: str, bottomaoe: str, bottomquest: str) -> Image:

    card = load_ability_card_background()
    card = tint(card, *color)
    font = load_font(size=_CARD_TITLE_SIZE)
    draw_text(text=title, x=_CARD_TITLE_X, y=_CARD_TITLE_Y, image=card, font=font)

    initiative_font = load_font(size=_CARD_INITIATIVE_SIZE)
    draw_text(text=str(initiative), x=_CARD_INITIATIVE_X, y=_CARD_INITIATIVE_Y, image=card, font=initiative_font)

    text_font = load_font(size=_CARD_TEXT_SIZE)

    for i, tl in enumerate(toplines):
        ly = int(_CARD_TOP_TEXT_Y + ((_CARD_ICON_HEIGHT * _CARD_ICON_PADDING_Y) * i))
        draw_ability_line(card, tl, _CARD_TOP_TEXT_X, ly)

    for i, bl in enumerate(bottomlines):
        ly = int(_CARD_BOTTOM_TEXT_Y + ((_CARD_ICON_HEIGHT * _CARD_ICON_PADDING_Y) * i))
        draw_ability_line(card, bl, _CARD_BOTTOM_TEXT_X, ly)

    # draw level
    draw_text(text=str(level), x=_CARD_LEVEL_X, y=_CARD_LEVEL_Y, image=card, font=text_font)

    # draw loss icons
    if toploss:
        draw_icon(card, 'bigloss', x=_CARD_LOSS_X, y=_CARD_LOSS_TOP_Y)

    if bottomloss:
        draw_icon(card, 'bigloss', x=_CARD_LOSS_X, y=_CARD_LOSS_BOTTOM_Y)

    return card
