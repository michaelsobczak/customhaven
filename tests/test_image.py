from gloomtools.image import load_font, load_ability_card_background, draw_text, tint, draw_ability_card
import gloomtools.image as gti

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

def test_draw_ability_card():
    card = draw_ability_card('Custom Card', 78, [
        "{attack} 3 {wound} target all adjacent enemies {dark}",
        "{attack} 3 {range} 2 {wind} {fire}",
    ],[
        "{attack} 3 {wound} target all adjacent enemies {dark}",
        "{attack} 3 {range} 2 {wind} {fire}",
    ], (155,251,152,255), 4, True, True, 'infinite_lifetime', '', '', 'round_lifetime', '', '')
    card.show()

def test_load_icon():
    assert gti.load_icon('wound')