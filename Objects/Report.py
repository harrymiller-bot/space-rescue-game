from GameFrame import RoomObject, Globals



class Report(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Block.png")
        self.set_image(image,240,240)
        self.handle_mouse_events = True

    def clicked(self, button_number):
        if button_number != 1:
            return

        Globals.response = False

        mail_obj = getattr(self.room, 'text', None)
        is_scam = getattr(mail_obj, 'is_scam', False)

        if is_scam:
            Globals.money += 50
        else:
            Globals.money -= 50

        self.room.running = False
        Globals.next_level = 1

