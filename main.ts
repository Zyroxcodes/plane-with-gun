controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    projectile = sprites.createProjectileFromSprite(assets.image`
        laser1
    `, mySprite, 300, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy(effects.fire, 500)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
    scene.cameraShake(4, 500)
})
let bogey : Sprite = null
let projectile : Sprite = null
let mySprite : Sprite = null
scene.setBackgroundImage(assets.image`
    background 1
`)
mySprite = sprites.create(assets.image`
    plane
`, SpriteKind.Player)
controller.moveSprite(mySprite)
mySprite.setStayInScreen(true)
info.setLife(3)
game.onUpdateInterval(500, function on_update_interval() {
    
    bogey = sprites.create(assets.image`
        bogey1
    `, SpriteKind.Enemy)
    bogey.setVelocity(-100, 0)
    bogey.setPosition(160, randint(5, 115))
    bogey.setFlag(SpriteFlag.AutoDestroy, true)
})
