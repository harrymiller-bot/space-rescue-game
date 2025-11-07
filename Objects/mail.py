from GameFrame import RoomObject

class mail(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("mail.jpg")
        self.set_image(image,183,131)

        self.handle_mouse_events = True

    def clicked(self, button_number):
        if button_number == 1:
            self.room.running = False