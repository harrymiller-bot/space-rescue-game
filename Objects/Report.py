from GameFrame import RoomObject, Globals
from Objects.text import scam


class Report(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Block.png")
        self.set_image(image,240,240)
        self.handle_mouse_events = True

    def clicked(self, button_number):
        Response = True
        self.room.running = False
        Globals.next_level = 1

        if scam == True and Response == True or scam == False and Response == False: 
            Globals.money += 50


