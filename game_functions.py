import sys;
import pygame;
from peashooter import Peashooter;
from bullet import Bullet;
from zombie import Zombie;
from pygame.sprite import Group, groupcollide;
import random;

def check_events(screen,game_settings,squares,plants,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit();
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos();
			for square in squares:
				if square.rect.collidepoint(mouse_x,mouse_y):
					print "Square: ",square.square_number;
					plants.add(Peashooter(screen,square));
			# print mouse_x;
			# print mouse_y;

def update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick):
	screen.blit(background.image,background.rect);

	for zombie in zombies.sprites():
		zombie.rect.centery = squares['rows'][random.randint(0,4)];
		zombie.update_me();
		zombie.draw_me();
	if tick % 10 == 0:
		zombies.add(Zombie(screen,game_settings.zombie_speed,game_settings.zombie_health));
	zombie_died = groupcollide(zombies, bullets, True, True);

	for plant in plants.sprites():
		# plant.update_me();
		plant.draw_me();
		if tick % 30 == 0:
			bullets.add(Bullet(screen,plant));
	plant_died = groupcollide(plants, zombies, True, False);

	for bullet in bullets.sprites():
		bullet.update_me();
		bullet.draw_me();