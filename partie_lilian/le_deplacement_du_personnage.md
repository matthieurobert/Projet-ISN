import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()
pygame.key.set_repeat(50, 15)

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_d:	#Si "flèche bas"
				#On descend le perso
				position_perso = position_perso.move(0,6)
		if event.type == KEYDOWN:
			if event.key == K_e:	#Si "flèche haut"
				#On monte le perso
				position_perso = position_perso.move(0,-6)
		if event.type == KEYDOWN:
			if event.key == K_f:	#Si "flèche de droite"
				#On fait déplacer notre personnonage vers la droit
				position_perso = position_perso.move(6,0)
		if event.type == KEYDOWN:
			if event.key == K_s:	#Si "flèche de gauche"
				#On fait déplacer notre personnonage vers la gauche
				position_perso = position_perso.move(-6,0)
#Re-collage
	fenetre.blit(fond, (0,0))
	fenetre.blit(perso, position_perso)
	#Rafraichissement
	pygame.display.flip()
#BOUTON POUR SE DIRIGER E haut D bat S gauche F droit
	