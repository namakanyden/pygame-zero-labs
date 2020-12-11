from pgzero.builtins import Actor
from settings import WIDTH, HEIGHT


class Brick(Actor):
    def __init__(self):
        super(Brick, self).__init__('brick.red')
