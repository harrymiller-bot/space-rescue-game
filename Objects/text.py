from GameFrame import TextObject, Globals
import random

class text(TextObject):
    def __init__(self, room, x: int, y: int, text=None):
        TextObject.__init__(self, room, x, y, text)

        self.size = 30
        self.font = 'Arial Black'
        self.bold = False
        self.colour = (0, 0, 0)

        if random.random() < 0.5:
            msg = self.get_message_good()
            self.is_scam = False
        else:
            msg = self.get_message_bad()
            self.is_scam = True

        self.text = msg if msg is not None else "No messages available"
        self.update_text()

    def get_message_good(self):
        if len(Globals.mail_messages_good) > 0:
            return Globals.mail_messages_good.pop(random.randrange(len(Globals.mail_messages_good)))
        return None

    def get_message_bad(self):
        if len(Globals.mail_messages_bad) > 0:
            return Globals.mail_messages_bad.pop(random.randrange(len(Globals.mail_messages_bad)))
        return None