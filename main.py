def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        laser1
    """), mySprite, 300, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.fire, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
scene.set_background_image(assets.image("""
    background 1
"""))
mySprite = sprites.create(assets.image("""
    plane
"""), SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
info.set_life(3)

def on_update_interval():
    global bogey
    bogey = sprites.create(assets.image("""
        bogey1
    """), SpriteKind.enemy)
    bogey.set_velocity(-100, 0)
    bogey.set_position(160, randint(5, 115))
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval)
