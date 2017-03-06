import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Snowpea(Plant):
	def __init__(self,screen,square):
		self.health = 5;
		self.shoot_speed = .5;
		self.image_file = "images/Snowpea.png";
		self.screen = screen;
		self.square = square;
		self.name = "snowpea";
		self.can_shoot = True;
		self.can_make_sun = False;
		self.sun_speed = 0;
		self.sun_cost = 100;

		super(Snowpea,self).__init__();
