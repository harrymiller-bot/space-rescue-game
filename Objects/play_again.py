from GameFrame import RoomObject, Globals
from Objects.Money import Money

class play_again(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("play_again.png")
        self.set_image(image,338,397)

        self.handle_mouse_events = True

    def clicked(self, button_number):
        if button_number == 1:
            self.room.running = False
            Globals.next_level = 0
            Globals.money = 0
            Globals.mail_messages_good = Globals.mail_messages_good_R.copy()
            Globals.mail_messages_bad = Globals.mail_messages_bad_R.copy()
            

