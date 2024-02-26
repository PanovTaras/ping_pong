import pygame
import sys
from random import randint 
pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Ping_Pong.Taras_production')


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

ball = Ball('real_black_ball.png', 100, 400, 3, 110, 110)                                                                                                                                                                                        

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	ball.reset()
	ball.update()
	pygame.display.update()
	window.fill((255, 255, 255))
	clock.tick(60) 