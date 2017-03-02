import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Sunflower(Plant):
	def __init__(self,screen,square):
		self.health = 6;
		self.shoot_speed = 999;
		self.image_file = "images/sunflower.png";
		self.screen = screen;
		self.square = square;
		self.name = "sunflower";

		super(Sunflower,self).__init__();
