from gloomtools.image import load_font, load_ability_card_background, draw_text, tint


def test_load_font():
    font = load_font()
    assert font

def test_ability_bg_load():
    assert load_ability_card_background()

def test_draw_ability_title():
    img = load_ability_card_background()
    draw_text('Card Title', x=120, y=10, image=img, font=load_font(size=40))

def test_ability_tint():
    img = load_ability_card_background()
    assert tint(img, 152,251,152, 255)