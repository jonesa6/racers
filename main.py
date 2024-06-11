@namespace
class SpriteKind:
    c = SpriteKind.create()
    car = SpriteKind.create()
    car2 = SpriteKind.create()
    coll = SpriteKind.create()
# a racer game with  2 AIs
# fetaures
# AI basic ai that computes two sprites.
# win lose decection.
# smart AI but AI has to collide to dectect the obstacle.
# crashing
# respawning
# how ai works. the ai checks the tiles above it below it and in front of it. then it will set the sprites vx and vy to advoid the obstacle. it can't solve everything because the vy is preprogramed. not ever changed when playing the game.

def on_overlap_tile(sprite, location):
    game.set_game_over_message(False, "ai 2 wins")
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.car2,
    assets.tile("""
        myTile
    """),
    on_overlap_tile)

# Start or complete respawn
def startreswan():
    global mySprite5, mySprite, mySprite2, mySprite3
    mySprite5 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.coll)
    mySprite = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . 2 2 2 2 2 2 2 2 . . . . 
                    . . . 2 4 2 2 2 2 2 2 c 2 . . . 
                    . . 2 c 4 2 2 2 2 2 2 c c 2 . . 
                    . 2 c c 4 4 4 4 4 4 2 c c 4 2 d 
                    . 2 c 2 e e e e e e e b c 4 2 2 
                    . 2 2 e b b e b b b e e b 4 2 2 
                    . 2 e b b b e b b b b e 2 2 2 2 
                    . e e 2 2 2 e 2 2 2 2 2 e 2 2 2 
                    . e e e e e e f e e e f e 2 d d 
                    . e e e e e e f e e f e e e 2 d 
                    . e e e e e e f f f e e e e e e 
                    . e f f f f e e e e f f f e e e 
                    . . f f f f f e e f f f f f e . 
                    . . . f f f . . . . f f f f . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . 9 9 9 9 9 9 9 9 . . . . 
                    . . . 2 9 9 9 9 9 9 9 c 2 . . . 
                    . . 2 c 9 9 9 9 9 9 9 c c 2 . . 
                    . 9 c c 9 9 9 9 9 9 9 c c 4 9 d 
                    . 9 c 2 9 9 9 9 9 9 9 b c 4 9 9 
                    . 9 9 e 9 9 9 9 9 9 9 9 b 4 9 9 
                    . 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                    . 9 9 2 2 2 9 2 2 2 2 2 9 9 9 9 
                    . 9 9 9 9 9 9 f 9 9 9 f 9 9 d d 
                    . 9 9 9 9 9 9 f 9 9 f 9 9 9 2 d 
                    . 9 9 9 9 9 9 f f f 9 9 9 9 9 9 
                    . 9 f f f f 9 9 9 9 f f f 9 9 9 
                    . . f f f f f 9 9 f f f f f 9 . 
                    . . . f f f . . . . f f f f . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.car)
    mySprite3 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . 6 6 6 6 6 6 6 6 . . . . 
                    . . . 6 9 6 6 6 6 6 6 c 6 . . . 
                    . . 6 c 9 6 6 6 6 6 6 c c 6 . . 
                    . 6 c c 9 9 9 9 9 9 6 c c 9 6 d 
                    . 6 c 6 8 8 8 8 8 8 8 b c 9 6 6 
                    . 6 6 8 b b 8 b b b 8 8 b 9 6 6 
                    . 6 8 b b b 8 b b b b 8 6 6 6 6 
                    . 8 8 6 6 6 8 6 6 6 6 6 8 6 6 6 
                    . 8 8 8 8 8 8 f 8 8 8 f 8 6 d d 
                    . 8 8 8 8 8 8 f 8 8 f 8 8 8 6 d 
                    . 8 8 8 8 8 8 f f f 8 8 8 8 8 8 
                    . 8 f f f f 8 8 8 8 f f f 8 8 8 
                    . . f f f f f 8 8 f f f f f 8 . 
                    . . . f f f . . . . f f f f . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.car2)
    mySprite.y = 120
    mySprite2.y = 60
    mySprite3.y = 90
    mySprite2.set_velocity(50, 0)
    mySprite3.set_velocity(100, 0)
    mySprite.set_velocity(30, 0)
    controller.move_sprite(mySprite, 120, 120)
    scene.camera_follow_sprite(mySprite)
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
# operate basic AI with some fixes. operates two sprites with AI
def basic_AI():
    # ai 1 basic AI
    if mySprite2.is_hitting_tile(CollisionDirection.RIGHT) and mySprite2.is_hitting_tile(CollisionDirection.LEFT):
        mySprite2.set_velocity(0, -50)
    elif mySprite2.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite2.set_velocity(0, -50)
    elif mySprite2.is_hitting_tile(CollisionDirection.RIGHT) and mySprite2.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite2.set_velocity(0, 50)
    elif mySprite2.is_hitting_tile(CollisionDirection.RIGHT) or mySprite2.is_hitting_tile(CollisionDirection.TOP):
        mySprite2.set_velocity(0, 50)
    else:
        mySprite2.set_velocity(randint(70, 80), 0)
    # ai 2 basic AI
    if not (mySprite3.is_hitting_tile(CollisionDirection.RIGHT) or mySprite3.is_hitting_tile(CollisionDirection.TOP) or mySprite3.is_hitting_tile(CollisionDirection.BOTTOM)):
        mySprite3.set_velocity(randint(70, 80), 0)
    elif mySprite2.is_hitting_tile(CollisionDirection.RIGHT) and mySprite2.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite3.set_velocity(0, -50)
    elif mySprite3.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite3.set_velocity(0, -50)
    elif mySprite3.is_hitting_tile(CollisionDirection.RIGHT) or mySprite3.is_hitting_tile(CollisionDirection.TOP):
        mySprite3.set_velocity(0, 50)
    elif mySprite2.is_hitting_tile(CollisionDirection.RIGHT) and mySprite2.is_hitting_tile(CollisionDirection.LEFT):
        mySprite3.set_velocity(0, -50)

def on_hit_wall(sprite5, location4):
    global cll
    if True:
        cll = True
    else:
        cll = False
scene.on_hit_wall(SpriteKind.coll, on_hit_wall)

def on_on_overlap(sprite7, otherSprite3):
    sprites.destroy(mySprite, effects.fire, 100)
    sprites.destroy(mySprite2, effects.fire, 100)
    sprites.destroy(mySprite3, effects.fire, 100)
    
    def on_after():
        startreswan()
    timer.after(1000, on_after)
    
sprites.on_overlap(SpriteKind.player, SpriteKind.car2, on_on_overlap)

def on_overlap_tile2(sprite4, location3):
    game.set_game_over_message(True, "you win!")
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile2)

def startrespawn2():
    global mySprite2, mySprite3
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . 9 9 9 9 9 9 9 9 . . . . 
                    . . . 2 9 9 9 9 9 9 9 c 2 . . . 
                    . . 2 c 9 9 9 9 9 9 9 c c 2 . . 
                    . 9 c c 9 9 9 9 9 9 9 c c 4 9 d 
                    . 9 c 2 9 9 9 9 9 9 9 b c 4 9 9 
                    . 9 9 e 9 9 9 9 9 9 9 9 b 4 9 9 
                    . 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                    . 9 9 2 2 2 9 2 2 2 2 2 9 9 9 9 
                    . 9 9 9 9 9 9 f 9 9 9 f 9 9 d d 
                    . 9 9 9 9 9 9 f 9 9 f 9 9 9 2 d 
                    . 9 9 9 9 9 9 f f f 9 9 9 9 9 9 
                    . 9 f f f f 9 9 9 9 f f f 9 9 9 
                    . . f f f f f 9 9 f f f f f 9 . 
                    . . . f f f . . . . f f f f . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.car)
    mySprite3 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . 6 6 6 6 6 6 6 6 . . . . 
                    . . . 6 9 6 6 6 6 6 6 c 6 . . . 
                    . . 6 c 9 6 6 6 6 6 6 c c 6 . . 
                    . 6 c c 9 9 9 9 9 9 6 c c 9 6 d 
                    . 6 c 6 8 8 8 8 8 8 8 b c 9 6 6 
                    . 6 6 8 b b 8 b b b 8 8 b 9 6 6 
                    . 6 8 b b b 8 b b b b 8 6 6 6 6 
                    . 8 8 6 6 6 8 6 6 6 6 6 8 6 6 6 
                    . 8 8 8 8 8 8 f 8 8 8 f 8 6 d d 
                    . 8 8 8 8 8 8 f 8 8 f 8 8 8 6 d 
                    . 8 8 8 8 8 8 f f f 8 8 8 8 8 8 
                    . 8 f f f f 8 8 8 8 f f f 8 8 8 
                    . . f f f f f 8 8 f f f f f 8 . 
                    . . . f f f . . . . f f f f . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.car2)
    mySprite2.y = 60
    mySprite3.y = 90
    mySprite2.set_velocity(50, 0)
    mySprite3.set_velocity(100, 0)
    mySprite.set_velocity(30, 0)
    tiles.set_current_tilemap(tilemap("""
        level2
    """))

def on_overlap_tile3(sprite2, location2):
    game.set_game_over_message(False, "ai 1 wins")
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.car,
    assets.tile("""
        myTile
    """),
    on_overlap_tile3)

def on_on_overlap2(sprite3, otherSprite):
    sprites.destroy(mySprite2, effects.fire, 100)
    sprites.destroy(mySprite3, effects.fire, 100)
    
    def on_after2():
        startrespawn2()
    timer.after(1000, on_after2)
    
sprites.on_overlap(SpriteKind.car, SpriteKind.car2, on_on_overlap2)

def on_on_overlap3(sprite6, otherSprite2):
    sprites.destroy(mySprite, effects.fire, 100)
    sprites.destroy(mySprite2, effects.fire, 100)
    sprites.destroy(mySprite3, effects.fire, 100)
    
    def on_after3():
        startreswan()
    timer.after(1000, on_after3)
    
sprites.on_overlap(SpriteKind.player, SpriteKind.car, on_on_overlap3)

# start the game
cll = False
mySprite3: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
mySprite5: Sprite = None
music.play(music.create_song(hex("""
        00780004080200
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
startreswan()
# waits a random amount of time. then run AI code

def on_update_interval():
    basic_AI()
game.on_update_interval(randint(15, 30), on_update_interval)

def on_on_update():
    if not (controller.any_button.is_pressed()):
        mySprite.set_velocity(randint(80, 90), 0)
game.on_update(on_on_update)
