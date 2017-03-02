import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Wallnut(Plant):
	def __init__(self,screen,square):
		self.health = 6;
		self.shoot_speed = 999;
		self.image_file = "images/wallnut.png";
		self.screen = screen;
		self.square = square;
		self.name = "wallnut";

		super(Wallnut,self).__init__();
