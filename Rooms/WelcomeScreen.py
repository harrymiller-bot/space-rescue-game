from GameFrame import Level
from Objects.start import Start_button

class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("Title.png")

        self.add_room_object(Start_button(self, 442, 735))
