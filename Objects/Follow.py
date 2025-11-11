from GameFrame import RoomObject

class Follow(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Follow.png")
        self.set_image(image,463,295)