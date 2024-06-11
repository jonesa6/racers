namespace SpriteKind {
    export const c = SpriteKind.create()
    export const car = SpriteKind.create()
    export const car2 = SpriteKind.create()
    export const coll = SpriteKind.create()
}
/**
 * start the game
 */
// a racer game with  2 AIs
// fetaures
// AI basic ai that computes two sprites.
// win lose decection.
// smart AI but AI has to collide to dectect the obstacle.
// crashing
// respawning
// how ai works. the ai checks the tiles above it below it and in front of it. then it will set the sprites vx and vy to advoid the obstacle. it can't solve everything because the vy is preprogramed. not ever changed when playing the game.
scene.onOverlapTile(SpriteKind.car2, assets.tile`myTile`, function (sprite, location) {
    game.setGameOverMessage(false, "ai 2 wins")
    game.gameOver(false)
})
// Start or complete respawn
function startreswan () {
    mySprite5 = sprites.create(img`
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
        `, SpriteKind.coll)
    mySprite = sprites.create(img`
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
        `, SpriteKind.Player)
    mySprite2 = sprites.create(img`
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
        `, SpriteKind.car)
    mySprite3 = sprites.create(img`
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
        `, SpriteKind.car2)
    mySprite.y = 120
    mySprite2.y = 60
    mySprite3.y = 90
    mySprite2.setVelocity(50, 0)
    mySprite3.setVelocity(100, 0)
    mySprite.setVelocity(30, 0)
    controller.moveSprite(mySprite, 120, 120)
    scene.cameraFollowSprite(mySprite)
    tiles.setCurrentTilemap(tilemap`level2`)
}
// operate basic AI with some fixes. operates two sprites with AI
function basic_AI () {
    // ai 1 basic AI
    if (mySprite2.isHittingTile(CollisionDirection.Right) && mySprite2.isHittingTile(CollisionDirection.Left)) {
        mySprite2.setVelocity(0, -50)
    } else if (mySprite2.isHittingTile(CollisionDirection.Bottom)) {
        mySprite2.setVelocity(0, -50)
    } else if (mySprite2.isHittingTile(CollisionDirection.Right) && mySprite2.isHittingTile(CollisionDirection.Bottom)) {
        mySprite2.setVelocity(0, 50)
    } else if (mySprite2.isHittingTile(CollisionDirection.Right) || mySprite2.isHittingTile(CollisionDirection.Top)) {
        mySprite2.setVelocity(0, 50)
    } else {
        mySprite2.setVelocity(randint(70, 80), 0)
    }
    // ai 2 basic AI
    if (!(mySprite3.isHittingTile(CollisionDirection.Right) || mySprite3.isHittingTile(CollisionDirection.Top) || mySprite3.isHittingTile(CollisionDirection.Bottom))) {
        mySprite3.setVelocity(randint(70, 80), 0)
    } else if (mySprite2.isHittingTile(CollisionDirection.Right) && mySprite2.isHittingTile(CollisionDirection.Bottom)) {
        mySprite3.setVelocity(0, -50)
    } else if (mySprite3.isHittingTile(CollisionDirection.Bottom)) {
        mySprite3.setVelocity(0, -50)
    } else if (mySprite3.isHittingTile(CollisionDirection.Right) || mySprite3.isHittingTile(CollisionDirection.Top)) {
        mySprite3.setVelocity(0, 50)
    } else if (mySprite2.isHittingTile(CollisionDirection.Right) && mySprite2.isHittingTile(CollisionDirection.Left)) {
        mySprite3.setVelocity(0, -50)
    }
}
scene.onHitWall(SpriteKind.coll, function (sprite5, location4) {
    if (true) {
        cll = true
    } else {
        cll = false
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.car2, function (sprite7, otherSprite3) {
    sprites.destroy(mySprite, effects.fire, 100)
    sprites.destroy(mySprite2, effects.fire, 100)
    sprites.destroy(mySprite3, effects.fire, 100)
    timer.after(1000, function () {
        startreswan()
    })
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite4, location3) {
    game.setGameOverMessage(true, "you win!")
    game.gameOver(true)
})
function startrespawn2 () {
    mySprite2 = sprites.create(img`
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
        `, SpriteKind.car)
    mySprite3 = sprites.create(img`
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
        `, SpriteKind.car2)
    mySprite2.y = 60
    mySprite3.y = 90
    mySprite2.setVelocity(50, 0)
    mySprite3.setVelocity(100, 0)
    mySprite.setVelocity(30, 0)
    tiles.setCurrentTilemap(tilemap`level2`)
}
scene.onOverlapTile(SpriteKind.car, assets.tile`myTile`, function (sprite2, location2) {
    game.setGameOverMessage(false, "ai 1 wins")
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.car, SpriteKind.car2, function (sprite3, otherSprite) {
    sprites.destroy(mySprite2, effects.fire, 100)
    sprites.destroy(mySprite3, effects.fire, 100)
    timer.after(1000, function () {
        startrespawn2()
    })
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.car, function (sprite6, otherSprite2) {
    sprites.destroy(mySprite, effects.fire, 100)
    sprites.destroy(mySprite2, effects.fire, 100)
    sprites.destroy(mySprite3, effects.fire, 100)
    timer.after(1000, function () {
        startreswan()
    })
})
let cll = false
let mySprite3: Sprite = null
let mySprite2: Sprite = null
let mySprite: Sprite = null
let mySprite5: Sprite = null
startreswan()
// waits a random amount of time. then run AI code
game.onUpdateInterval(randint(15, 30), function () {
    basic_AI()
})
game.onUpdate(function () {
    if (!(controller.anyButton.isPressed())) {
        mySprite.setVelocity(randint(80, 90), 0)
    }
})
//end of code