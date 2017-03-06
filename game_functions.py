import sys;
import pygame;
from peashooter import Peashooter;
from gatling import Gatling;
from repeater import Repeater;
from sunflower import Sunflower;
from wallnut import Wallnut;
from snowpea import Snowpea;
from bullet import Bullet;
from zombie import Zombie;
from pygame.sprite import groupcollide;
import random;
import time;

def check_events(screen,game_settings,squares,plants,bullets,icons):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit();
		if game_settings.game_active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y = pygame.mouse.get_pos();
				for square in squares:
					if square.plant_here == False:
						if square.rect.collidepoint(mouse_x,mouse_y):
							# print "Square: ",square.square_number;
							if(game_settings.chosen_plant == 1):
								sunflower = Sunflower(screen,square)
								if game_settings.total_sun >= sunflower.sun_cost:
									plants.add(sunflower);
									square.plant_here = True;
									game_settings.total_sun -= sunflower.sun_cost;
							elif(game_settings.chosen_plant == 2):
								peashooter = Peashooter(screen,square)
								if game_settings.total_sun >= peashooter.sun_cost:
									plants.add(peashooter);
									square.plant_here = True;						
									game_settings.total_sun -= peashooter.sun_cost;
							elif(game_settings.chosen_plant == 3):
								snowpea = Snowpea(screen,square)
								if game_settings.total_sun >= snowpea.sun_cost:
									plants.add(snowpea);
									square.plant_here = True;						
									game_settings.total_sun -= snowpea.sun_cost;
							elif(game_settings.chosen_plant == 4):
								repeater = Repeater(screen,square)
								if game_settings.total_sun >= repeater.sun_cost:
									plants.add(repeater);
									square.plant_here = True;
									game_settings.total_sun -= repeater.sun_cost;
							elif(game_settings.chosen_plant == 5):
								gatling = Gatling(screen,square)
								if game_settings.total_sun >= gatling.sun_cost:
									plants.add(gatling);
									square.plant_here = True;
									game_settings.total_sun -= gatling.sun_cost;
							elif(game_settings.chosen_plant == 6):
								wallnut = Wallnut(screen,square)
								if game_settings.total_sun >= wallnut.sun_cost:
									plants.add(wallnut);
									square.plant_here = True;
									game_settings.total_sun -= wallnut.sun_cost;
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
		if game_settings.game_active:
			zombie.update_me();
			zombie.draw_me();
		if zombie.rect.left <= zombie.screen_rect.left:
			game_settings.game_active = False;
		zombie.moving = True;

	if tick % 60 == 0:
		if pygame.time.get_ticks() >= 30000:
			zombies.add(Zombie(screen,game_settings));
	for plant in plants.sprites():
		# plant.update_me();
		plant.draw_me();
		# if tick % 30 == 0:
		should_shoot = time.time() - plant.last_shot > plant.shoot_speed;
		should_repeat = time.time() - plant.last_shot > (plant.shoot_speed/2);
		can_shoot = plant.can_shoot;
		in_my_row = game_settings.zombie_in_row[plant.yard_row] > 0
		if pygame.time.get_ticks() >= 30000:
			if should_shoot and in_my_row and can_shoot:
				bullets.add(Bullet(screen,plant));
				if plant.name == 'repeater':
					if should_repeat:
						bullets.add(Bullet(screen,plant));
				plant.last_shot = time.time();
		# plant_died = groupcollide(plants, zombies, True, False);
		can_make_sun = plant.can_make_sun;
		should_make_sun = time.time() - plant.last_sun > plant.sun_speed;
		if can_make_sun and should_make_sun:
			plant.make_sun(game_settings);
			plant.last_sun = time.time();

	for bullet in bullets.sprites():
		if game_settings.game_active:
			bullet.update_me();
		bullet.draw_me();

	score_font = pygame.font.SysFont("monospace",36);
	score_render = score_font.render("Zombies Killed: "+str(game_settings.zombies_killed) +"!",1,(255,215,0));
	screen.blit(score_render,(100,100));

	sun_render = score_font.render("Sun: "+str(game_settings.total_sun) +"!",1,(255,215,0));
	screen.blit(sun_render,(100,150));