from GameFrame import RoomObject

class mail(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("mail.jpg")
        self.set_image(image,183,131)