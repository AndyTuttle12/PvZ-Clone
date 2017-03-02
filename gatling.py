import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Gatling(Plant):
	def __init__(self,screen,square):
		self.health = 6;
		self.shoot_speed = .5;
		self.image_file = "images/Gatling_Pea_Fixed.png";
		self.screen = screen;
		self.square = square;
		self.name = "gatling";

		super(Gatling,self).__init__();
