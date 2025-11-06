from GameFrame import RoomObject

class shop(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("shop_icon.jpg")
        self.set_image(image,124,125)