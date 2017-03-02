import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Wallnut(Plant):
	def __init__(self,screen,square):
		self.health = 15;
		self.shoot_speed = 1;
		self.image_file = "images/wallnut.png";
		self.screen = screen;
		self.square = square;
		self.name = "wallnut";
		self.can_shoot = False;
		self.can_make_sun = False;
		self.sun_speed = 0;
		self.sun_cost = 50;

		super(Wallnut,self).__init__();
