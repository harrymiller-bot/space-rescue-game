from GameFrame import TextObject, Globals
import random

class text(TextObject):
    def __init__(self, room, x: int, y: int, text=None):       
        TextObject.__init__(self, room, x, y, text)
        
        self.size = 40
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.text = self.get_message()
        self.update_text()

    def get_message(self):
        return Globals.mail_messages.pop(random.randrange(len(Globals.mail_messages)))