from GameFrame import TextObject, Globals

class Money(TextObject):
    def __init__(self, room, x: int, y: int):       
        money_text = f"Money: ${Globals.money}"
        TextObject.__init__(self, room, x, y, money_text)
        
        self.size = 30
        self.font = 'Arial Black'
        self.colour = (0, 0, 0)
        self.bold = False
        self.update_text()