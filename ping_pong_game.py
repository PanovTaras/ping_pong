import pygame
import sys
from random import randint 
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 70)

clock = pygame.time.Clock()
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Ping_Pong.Taras_production')

victory = False

class Game_sprite(pygame.sprite.Sprite):
	def  __init__(self,player_image, player_x, player_y, player_speed, player_height, player_width):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load(player_image), (player_width, player_height))
		self.speed_x = player_speed
		self.speed_y = player_speed
		self.rect  = self.image.get_rect()
		self.rect.x = player_x
		self.rect.y = player_y
		self.rect.height = player_height
		self.rect.width = player_width

	def reset(self):
		window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(Game_sprite):
	def update(self):
		self.rect.x += self.speed_x  
		self.rect.y += self.speed_y
		if self.rect.y >= 500 - 99: 
			self.speed_y *= -1
		elif self.rect.y <= 0:
			self.speed_y *= -1
	def start_possition(self):
		self.rect.x = 295
		self.rect.y = 195
		self.speed_x *= -1
		self.speed_y *= -1

class Player(Game_sprite):
	def  __init__(self,player_image, player_x, player_y, player_speed, player_height, player_width):
		super().__init__(player_image, player_x, player_y, player_speed, player_height, player_width)
		self.scor = 0	
	def update_l(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w] and self.rect.y > 0:
			self.rect.y -= self.speed_y
		if keys[pygame.K_s] and self.rect.y < 300:
			self.rect.y += self.speed_y

	def update_r(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP] and self.rect.y > 0:
			self.rect.y -= self.speed_y
		if keys[pygame.K_DOWN] and self.rect.y < 300:
			self.rect.y += self.speed_y

ball = Ball('real_black_ball.png', 100, 400, 3, 110, 110)                                                                                                                                                                                        
wall_right = Player('real_black_wall.jpg', 600, 100, 5, 200, 75)
wall_left = Player('real_black_wall.jpg', 25, 100, 5, 200, 75)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	if victory != True:		
		ball.reset()
		wall_right.reset()
		wall_left.reset()
		ball.update()
		wall_right.update_r()
		wall_left.update_l()
		if pygame.sprite.collide_rect(wall_right, ball) or pygame.sprite.collide_rect(wall_left, ball):
			ball.speed_x *= -1
		if ball.rect.x <= -110:
			wall_right.scor += 1
			ball.start_possition()
		elif ball.rect.x >= 700:
			wall_left.scor += 1
			ball.start_possition()
		if wall_right.scor >= 3:
			win = font.render('YOU WIN! PLAYER_1', True, (0, 0, 0))
			window.blit(win, (100, 200))
			victory = True
		if wall_left.scor >= 3:
			win = font.render('YOU WIN! PLAYER_2', True, (0, 0, 0))
			window.blit(win, (100, 200))
			victory = True			
		pygame.display.update()
		window.fill((255, 255, 255))
		clock.tick(60)
