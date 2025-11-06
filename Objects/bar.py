from GameFrame import RoomObject

class Bar(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("bar.webp")
        self.set_image(image,1200,200)