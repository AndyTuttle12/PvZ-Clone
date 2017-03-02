import sys;
import pygame;
from peashooter import Peashooter;
from gatling import Gatling;
from repeater import Repeater;
from sunflower import Sunflower;
from wallnut import Wallnut;
from bullet import Bullet;
from zombie import Zombie;
from pygame.sprite import groupcollide;
import random;
import time;

def check_events(screen,game_settings,squares,plants,bullets,icons):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit();
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos();
			for square in squares:
				if square.rect.collidepoint(mouse_x,mouse_y):
					# print "Square: ",square.square_number;
					if(game_settings.chosen_plant == 1):
						plants.add(Sunflower(screen,square));
					elif(game_settings.chosen_plant == 2):
						plants.add(Peashooter(screen,square));
					elif(game_settings.chosen_plant == 3):
						plants.add(Repeater(screen,square));
					elif(game_settings.chosen_plant == 4):
						plants.add(Gatling(screen,square));
					elif(game_settings.chosen_plant == 5):
						plants.add(Wallnut(screen,square));
				for icon in icons:
					if icon.rect.collidepoint(mouse_x,mouse_y):
						game_settings.chosen_plant = icon.slot
			# print mouse_x;
			# print mouse_y;
		elif event.type == pygame.MOUSEMOTION:
			# print event.pos;
			for square in squares:
				if square.rect.collidepoint(event.pos):
					game_settings.highlighted_square = square;
					# print game_settings.highlighted_square;

def update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick,icons):
	screen.blit(background.image,background.rect);

	for icon in icons:
		screen.blit(icon.image, icon.rect);

	if game_settings.highlighted_square != 0:
		pygame.draw.rect(screen,(255,215,0),(game_settings.highlighted_square.rect.left,game_settings.highlighted_square.rect.top,game_settings.squares['square_width'],game_settings.squares['square_height']),5);

	for zombie in zombies.sprites():
		zombie.update_me();
		zombie.draw_me();
		if zombie.rect.left <= zombie.screen_rect.left:
			game_settings.game_active = False;
	if tick % 30 == 0:
		zombies.add(Zombie(screen,game_settings));
	for plant in plants.sprites():
		# plant.update_me();
		plant.draw_me();
		# if tick % 30 == 0:
		if plant.name == 'sunflower' or plant.name == 'wallnut':
			should_shoot = False;
		else:
			should_shoot = time.time() - plant.last_shot > plant.shoot_speed;
		in_my_row = game_settings.zombie_in_row[plant.yard_row] > 0
		if should_shoot and in_my_row:
			bullets.add(Bullet(screen,plant));
			plant.last_shot = time.time();
			plant_died = groupcollide(plants, zombies, True, False);

	for bullet in bullets.sprites():
		bullet.update_me();
		bullet.draw_me();

	score_font = pygame.font.SysFont("monospace",36);
	score_render = score_font.render("Zombies Killed: "+str(game_settings.zombies_killed) +"!",1,(255,215,0));
	screen.blit(score_render,(100,100));