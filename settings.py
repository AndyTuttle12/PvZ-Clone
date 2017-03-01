import pygame;

class Settings():
	def __init__(self):
		display_info = pygame.display.Info();
		self.screen_size = (display_info.current_w,display_info.current_h);
		self.bg_color = (82,111,53);
		self.zombie_speed = .5;
		self.zombie_health = 5;
		self.squares = {
			"start_left": 428,
			"start_top": 280,
			"square_width": 135,
			"square_height": 120,
			"rows": [
				280,
				400,
				520,
				640,
				760
			]
		};
		self.highlighted_square = 0;
		self.zombie_in_row = [
			0,
			0,
			0,
			0,
			0
		];
		

