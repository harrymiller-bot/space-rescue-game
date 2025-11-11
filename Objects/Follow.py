from GameFrame import RoomObject, Globals
from Objects.text import scam

class Follow(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Follow.png")
        self.set_image(image,463,295)
        self.handle_mouse_events = True

    def clicked(self, button_number):
        Response = False
        self.room.running = False
        Globals.next_level = 1

        if scam == True and Response == False or scam == False and Response == True: 
            Globals.money -= 50
