import sys;
import pygame;
from peashooter import Peashooter;
from bullet import Bullet;
from zombie import Zombie;
from pygame.sprite import groupcollide;
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
		elif event.type == pygame.MOUSEMOTION:
			# print event.pos;
			for square in squares:
				if square.rect.collidepoint(event.pos):
					game_settings.highlighted_square = square;
					print game_settings.highlighted_square;

def update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick):
	screen.blit(background.image,background.rect);

	if game_settings.highlighted_square != 0:
		pygame.draw.rect(screen,(255,215,0),(game_settings.highlighted_square.rect.left,game_settings.highlighted_square.rect.top,game_settings.squares['square_width'],game_settings.squares['square_height']),5);

	for zombie in zombies.sprites():
		zombie.update_me();
		zombie.draw_me();
	if tick % 30 == 0:
		zombies.add(Zombie(screen,game_settings));
		# game_settings.row_zombies[plant.yard_row] += 1;
		# print game_settings.row_zombies[zombie.yard_row];
	for plant in plants.sprites():
		# plant.update_me();
		plant.draw_me();
		if tick % 30 == 0:
			if game_settings.zombie_in_row[plant.yard_row]:
				bullets.add(Bullet(screen,plant));
			plant_died = groupcollide(plants, zombies, True, False);

	for bullet in bullets.sprites():
		bullet.update_me();
		bullet.draw_me();