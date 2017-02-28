import pygame;
from settings import Settings;
import game_functions as gf;
from background import Background;
import sys;
from square import Square;



from pygame.sprite import Group, groupcollide;

pygame.init();
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption("A PvZ Clone");
background = Background(game_settings);

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
		gf.check_events(screen,game_settings,squares,plants,bullets);
		gf.update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick);
		tick += 1;
		pygame.display.flip();
run_game();