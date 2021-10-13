input.onButtonPressed(Button.A, function () {
    ORGÁNICO.set(LedSpriteProperty.X, 3)
    basic.pause(200)
    ORGÁNICO.set(LedSpriteProperty.Y, 3)
})
let ORGÁNICO: game.LedSprite = null
ORGÁNICO = game.createSprite(0, 0)
basic.forever(function () {
    basic.showLeds(`
        . . . . .
        . # . . #
        . # . . #
        . # . . #
        . # # # #
        `)
})
