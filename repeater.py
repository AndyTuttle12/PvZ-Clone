import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Repeater(Plant):
	def __init__(self,screen,square):
		self.health = 6;
		self.shoot_speed = .5;
		self.image_file = "images/repeater.png";
		self.screen = screen;
		self.square = square;
		self.name = "repeater";
		self.can_shoot = True;
		self.can_make_sun = False;
		self.sun_speed = 0;
		self.sun_cost = 200;

		super(Repeater,self).__init__();
