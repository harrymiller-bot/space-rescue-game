from GameFrame import TextObject, Globals

class Money(TextObject):
    def __init__(self, room, x: int, y: int):
        money_text = f"Money: ${Globals.money}"
        TextObject.__init__(self, room, x, y, money_text)

        self.size = 30
        self.font = 'Arial Black'
        self.colour = (0, 0, 0)
        self.bold = False

        self.prev_money = Globals.money
        self.update_text()

    def update(self):
        if Globals.money != self.prev_money:
            self.prev_money = Globals.money
            self.text = f"Money: ${Globals.money}"
            self.update_text()
        if Globals.money <= 0:
            self.colour = (255, 0, 0)
            self.update_text()
        else:
            self.colour = (0, 255, 0)
            self.update_text()

        
        if Globals.money >= Globals.threshold:
            self.running = False
            Globals.next_level = 3

        if Globals.money <= -200:
            self.running = False
            Globals.next_level = 4
        super().update()