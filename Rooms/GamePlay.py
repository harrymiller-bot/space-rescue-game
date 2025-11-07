from GameFrame import Level
from Objects.bar import Bar
from Objects.mail import mail
from Objects.Shop import shop

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("game_background.png")

        self.add_room_object(mail(self, 30, 645))
        self.add_room_object(mail(self, 230, 645))
        self.add_room_object(mail(self, 430, 645))
        self.add_room_object(shop(self, 30, 40))
        self.add_room_object(Bar(self, 0, 600))
        self.add_room_object(Bar(self, 0, 0))