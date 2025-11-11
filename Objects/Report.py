from GameFrame import RoomObject, Globals

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
