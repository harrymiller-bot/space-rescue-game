from GameFrame import TextObject, Globals
import random

class Goal(TextObject):
    def __init__(self, room, x: int, y: int, text=None):
        TextObject.__init__(self, room, x, y, text)

        self.size = 30
        self.font = 'Arial Black'
        self.bold = False
        self.colour = (0, 0, 0)
