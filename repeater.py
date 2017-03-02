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

		super(Repeater,self).__init__();
