from pgzero.builtins import Actor, keyboard
from settings import WIDTH, HEIGHT


class Paddle(Actor):
    def __init__(self):
        super(Paddle, self).__init__('paddle')
        self.x = WIDTH / 2
        self.bottom = HEIGHT
        self.speed = 3

    def update(self):
        # update paddle
        if keyboard.left == True:
            self.x = self.x - self.speed
            if self.left <= 0:
                self.left = 0

        if keyboard.right == True:
            self.x = self.x + self.speed
            if self.right >= WIDTH:
                self.right = WIDTH
