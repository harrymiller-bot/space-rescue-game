from GameFrame import TextObject, Globals
import random

scam = False

class text(TextObject):
    def __init__(self, room, x: int, y: int, text=None):       
        TextObject.__init__(self, room, x, y, text)
        
        self.size = 30
        self.font = 'Arial Black'
        self.colour = (0,0,0)
        self.bold = False
        
        if random.random() < 0.5:
            self.text = self.get_message_good()
            scam = False
        else:
            self.text = self.get_message_bad()
            scam = True
            
        if self.text is None:
            self.text = "No messages available"
            
        self.update_text()
        print(scam)

    def get_message_good(self):
        if len(Globals.mail_messages_good) > 0:
            return Globals.mail_messages_good.pop(random.randrange(len(Globals.mail_messages_good)))
        return None

    def get_message_bad(self):
        if len(Globals.mail_messages_bad) > 0:
            return Globals.mail_messages_bad.pop(random.randrange(len(Globals.mail_messages_bad)))
        return None