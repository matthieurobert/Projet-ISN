import pygame 
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1145,720), FULLSCREEN)

fond = pygame.image.load("background.png")
fenetre.blit(fond, (0 , 0))

player = pygame.image.load("sprite.png")
pos_player  = player.get_rect()
fenetre.blit(player, pos_player)


pygame.display.flip

continuer = 1 

while continuer:
	for event in pygame.event.get():
		

		while pos_player[1] < 720:
			pos_player = pos_player.move(0 , 3)

			fenetre.blit(fond, (0,0))
			fenetre.blit(player, pos_player)
			pygame.display.flip()

			if event.type == QUIT:
				continuer = 0 

		while pos_player[1] > 0:
			pos_player = pos_player.move(0 , -3)

			fenetre.blit(fond, (0,0))
			fenetre.blit(player, pos_player)
			pygame.display.flip()

			if event.type == QUIT:
				continuer = 0 