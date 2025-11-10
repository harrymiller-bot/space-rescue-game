from GameFrame import RoomObject

class Report(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("")
        self.set_image(image,124,125)