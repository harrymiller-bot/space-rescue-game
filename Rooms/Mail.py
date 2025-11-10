from GameFrame import Level, Globals
from Objects.text import text

class Mail(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("mail_back.jpg")

        # Create text object centered in screen
        self.text = text(self, 
                        Globals.SCREEN_WIDTH/2 - 200,  # Centered X position
                        Globals.SCREEN_HEIGHT/2 - 50,  # Centered Y position
                        "")
        self.add_room_object(self.text)