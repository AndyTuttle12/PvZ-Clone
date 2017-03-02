import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Sunflower(Plant):
	def __init__(self,screen,square):
		self.health = 5;
		self.shoot_speed = 1;
		self.image_file = "images/sunflower.png";
		self.screen = screen;
		self.square = square;
		self.name = "sunflower";
		self.can_shoot = False;
		self.can_make_sun = True;
		self.sun_speed = 10;
		self.sun_cost = 50;

		super(Sunflower,self).__init__();

	def make_sun(self,game_settings):
		game_settings.total_sun += 25;