from GameFrame import Level, Globals
from Objects.text import text

class Mail(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("mail_back.jpg")

        self.text = text(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, "")
        self.add_room_object(self.text)