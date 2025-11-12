from GameFrame import Level, Globals
from Objects.bar import Bar
from Objects.mail import mail
from Objects.Money import Money
from Objects.Goal import Goal

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("game_background.png")


        self.add_room_object(Money(self, 535, 50))
        self.add_room_object(mail(self, 500, 655))
        self.add_room_object(Goal(self, 360, 350, "Reach $1000 to win!"))
        self.add_room_object(Bar(self, 0, 600))
        self.add_room_object(Bar(self, 0, 0))
    



