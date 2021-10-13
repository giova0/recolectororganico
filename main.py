def on_button_pressed_a():
    ORGÁNICO.set(LedSpriteProperty.X, 3)
    basic.pause(200)
    ORGÁNICO.set(LedSpriteProperty.Y, 3)
input.on_button_pressed(Button.A, on_button_pressed_a)

ORGÁNICO: game.LedSprite = None
ORGÁNICO = game.create_sprite(0, 0)

def on_forever():
    basic.show_leds("""
        . . . . .
                . # . . #
                . # . . #
                . # . . #
                . # # # #
    """)
basic.forever(on_forever)
