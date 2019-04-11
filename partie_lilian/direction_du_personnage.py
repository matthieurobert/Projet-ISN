import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("perso.jpg").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()
pygame.key.set_repeat(50, 15)

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événementszz
		if event.type == QUIT:
			continuer = 0


		if event.type == KEYDOWN:  	#Si "flèche bas"
			if event.key == K_s:
				#On descend le perso
				position_perso = position_perso.move(0,6)
				print(position_perso[0])
			if event.key == K_w:
				#On monte le perso
				position_perso = position_perso.move(0,-6)
		if event.type == KEYDOWN:  #Si "flèche de droite"
			if event.key == K_d:
				#On fait déplacer notre personnonage vers la droit
				position_perso = position_perso.move(6,0)
				print("doite")
		if event.type == KEYDOWN:   #Si "flèche de gauche"
			if event.key == K_a:
				#On fait déplacer notre personnonage vers la gauche
				position_perso = position_perso.move(-6,0)


		if event.type == KEYDOWN:
			if event.key == K_a and event.key == K_w:
  	         #Si "flèche de gauche et fléche du haut"
				#On fait déplacer notre personnonage vers la gauche en haut

				position_perso = position_perso.move(-6,-6)


		if event.type == KEYDOWN:
			if event.key == K_a and event.key == K_s:
  	         #Si "flèche de gauche et fléche du bas"
				#On fait déplacer notre personnonage vers la gauche en bas
				position_perso = position_perso.move(-6,6)
		if event.type == KEYDOWN:
			if event.key == K_d and event.key == K_w:
  	         #Si "flèche de droite et fléche du haut"
				#On fait déplacer notre personnonage vers la gauche en haut
				position_perso = position_perso.move(6,-6)

		if event.type == KEYDOWN:
			if event.key == K_d and event.key == K_s:
  	         #Si "flèche de droite et fléche du bas"
				#On fait déplacer notre personnonage vers la gauche en haut
				position_perso = position_perso.move(6,6)


		if position_perso[0]<0:
				position_perso = position_perso.move(6,0)
		if position_perso[0]>550:
				position_perso = position_perso.move(-6,0)
		if position_perso[1]<0:
				position_perso = position_perso.move(0,6)
		if position_perso[1]>380:
				position_perso = position_perso.move(0,-6)





# BOUTON POUR SE DIRIGER E haut D bat S gauche F droit
	#Re-collage

	fenetre.blit(fond, (0,0))
	fenetre.blit(perso, position_perso)
	#Rafraichissement
	pygame.display.flip()
pygame.quit()