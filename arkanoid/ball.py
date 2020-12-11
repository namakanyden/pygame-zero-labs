from pgzero.builtins import Actor
from settings import WIDTH, HEIGHT


class Ball(Actor):
    def __init__(self):
        super(Ball, self).__init__('ball')
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.dx = 1
        self.dy = -1
        self.speed = 3

    def update(self):
        self.x = self.x + self.dx * self.speed
        self.y = self.y + self.dy * self.speed

        if self.top <= 0:
            self.dy = 1

        if self.right >= WIDTH:
            self.dx = -1

        if self.left <= 0:
            self.dx = 1

        if self.bottom >= HEIGHT:
            #ball.dy = -1
            print('You are Loser')
            quit()
