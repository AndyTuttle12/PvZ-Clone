import pygame;
from settings import Settings;
import game_functions as gf;
from background import Background;
from square import Square;
from zombie import Zombie;
from pygame.sprite import Group, groupcollide;
from plant_icon import Plant_Icon;
import time;

pygame.init();
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption("A PvZ Clone");
background = Background(game_settings);
sunflower_icon = Plant_Icon(game_settings,'sunflower-icon.png',1);
peashooter_icon = Plant_Icon(game_settings,'peashooter-icon.png',2);
snowpea_icon = Plant_Icon(game_settings,'snow_pea-icon.png',3);
repeater_icon = Plant_Icon(game_settings,'repeater-icon.png',4);
gatling_icon = Plant_Icon(game_settings,'gatling-icon.png',5);
wallnut_icon = Plant_Icon(game_settings,'wallnut-icon.png',6);
icons = [sunflower_icon,peashooter_icon,snowpea_icon,repeater_icon,gatling_icon,wallnut_icon];

zombies = Group();
plants = Group();
squares = Group();
bullets = Group();

for i in range(0,5):
	for j in range(0,9):
		squares.add(Square(screen,game_settings,i,j));

def run_game():
	tick = 0;

	while 1:
		gf.check_events(screen,game_settings,squares,plants,bullets,icons);
		if game_settings.game_active:
			tick += 1;
			zombies_hit = groupcollide(zombies, bullets, False, False);
			# print zombies_hit;
			for zombie in zombies_hit:
				# print zombie
				if zombie.yard_row == zombies_hit[zombie][0].yard_row:
					# print "Same row.";
					bullets.remove(zombies_hit[zombie][0]);
					zombie.hit(1);
					if zombie.health <= 0:
						zombies.remove(zombie);
						game_settings.zombie_in_row[zombie.yard_row] -= 1;
						game_settings.zombies_killed += 1;
			zombies_eating = groupcollide(zombies, plants, False, False);
			for zombie in zombies_eating:
				damaged_plant = zombies_eating[zombie][0];
				if zombie.yard_row == damaged_plant.yard_row:
					zombie.moving = False;
					if time.time() - zombie.started_eating > zombie.damage_time:
						zombie.zombie_chomp(damaged_plant);
						zombie.started_eating = time.time();
						if damaged_plant.health <= 0:
							plants.remove(damaged_plant);
							zombie.moving = True;
							damaged_plant.square.plant_here = False;

		gf.update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick,icons);
		pygame.display.flip();
run_game();