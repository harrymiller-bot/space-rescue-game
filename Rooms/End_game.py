from GameFrame import Level, Globals

class End_game(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("end_back.jpg")