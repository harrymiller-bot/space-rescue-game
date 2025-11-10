from GameFrame import RoomObject

class Follow(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("")
        self.set_image(image,124,125)