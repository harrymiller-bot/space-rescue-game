from GameFrame import Level, Globals
from Objects.play_again import play_again
class End_game(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("end_back.jpg")

        self.add_room_object(play_again(self, 331, 150))


