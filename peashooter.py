import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Peashooter(Plant):
	def __init__(self,screen,square):
		self.health = 5;
		self.shoot_speed = 1;
		self.image_file = "images/peashooter.png";
		self.screen = screen;
		self.square = square;
		self.name = "peashooter";

		super(Peashooter,self).__init__();
