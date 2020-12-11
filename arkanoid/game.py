#!/usr/bin/env pgzrun
from brick import Brick
from paddle import Paddle
from settings import WIDTH, HEIGHT, TITLE, ICON
from ball import Ball


# actors = []
ball = Ball()
paddle = Paddle()


# creating bricks
bricks = []
for i in range(10):
    brick = Brick()
    brick.left = brick.width * i
    bricks.append(brick)


def update():
    # update ball
    ball.update()

    if ball.colliderect(paddle):
        ball.dy = ball.dy * -1

    # update brick
    for brick in bricks:
        if ball.colliderect(brick) == True:
            bricks.remove(brick)
            ball.dy = ball.dy * -1
            break

    # well done
    if len(bricks) == 0:
        print('weel done')
        quit()

    paddle.update()

    # paddle.x = ball.x


def draw():
    screen.clear()

    for brick in bricks:
        brick.draw()

    ball.draw()
    paddle.draw()
