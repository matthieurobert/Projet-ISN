import pygame
import sys
from pygame.locals import *
from Partie_Clément.rekt_boîte import rekt

pygame.init()


rekt_boîte = rekt()
salle = rekt_boîte[-1::]
del rekt_boîte[-1:]


liste = salle[0]

fenetre = liste[0]
table = liste[1]
caisse = liste[2]
caisses = liste[3]
position_x_y = liste[4]


class ARBot(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Test_Matthieu/sprite.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect = self.image.get_rect()
		#self.side = side
		#self.speed = 10
		self.state = "still"
		self.newpos = [0, 0]
		self.speed = [0, 1]
		self.update()



	def update(self):
		if self.rect.left < 0 or self.rect.right > 1095:
			self.speed[1] = -self.speed[1]

		for d in range (0,len(rekt_boîte)):

			if self.rect.colliderect(rekt_boîte[d]):
				self.speed[1] = -self.speed[1]

		self.rect = self.rect.move(self.speed)

		#print(self.speed)

class LRBot(pygame.sprite.Sprite):



	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Test_Matthieu/sprite2.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect = pygame.Rect(0,200,50,50)
		#self.side = side
		#self.speed = 10
		self.state = "still"
		self.newpos = [0, 0]
		self.speed = [1, 0]
		self.update()


	def update(self):
		if self.rect.left < 0 or self.rect.right > 1095:
			self.speed[0] = -self.speed[0]

		for d in range (0,len(rekt_boîte)):

			if self.rect.colliderect(rekt_boîte[d]):
				self.speed[0] = -self.speed[0]

		self.rect = self.rect.move(self.speed)


		#print(self.speed)

perso = pygame.image.load("perso.jpg").convert()
position_perso = perso.get_rect()

speed =8
repouser = speed +1 
speed_diagonal = speed/2
time = 80
hauteur_x = 1100
hauteur_y= 675
fenetre.blit(perso, position_perso)
clock = pygame.time.Clock()
pygame.display.flip()
continuer = 0
pygame.key.set_repeat(50,15)

alien = ARBot()
pab = LRBot()

pygame.display.flip

continuer = 1

while continuer:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

 #alien.update()
    fenetre.blit(table, (0, 0))
    for i in range (0,caisses):
        b=position_x_y[i]
        x= b[0]
        y= b[1]
        fenetre.blit(caisse, (x,y))

    fenetre.blit( alien.image, alien.rect)
    fenetre.blit( pab.image, pab.rect)
    fenetre.blit(perso,position_perso)
    pab.update()

    pygame.display.flip()


    for event in pygame.event.get():
        key=pygame.key.get_pressed()
            

        if event.type == QUIT:
            continuer = 1
            pygame.quit()
        if  key[pygame.K_a] :
            clock.tick(time)             # gauche
            position_perso = position_perso.move(-speed,0)
            for d in range (0,len(rekt_boîte)):
                if position_perso.colliderect(rekt_boîte[d]):
                    position_perso = position_perso.move(repouser,0)


            if position_perso[0]<0:
                position_perso = position_perso.move(speed,0)
            if position_perso[0]>hauteur_x:
                position_perso = position_perso.move(-speed,0)
            if position_perso[1]<0:
                position_perso = position_perso.move(0,speed)
            if position_perso[1]>hauteur_y:
                position_perso = position_perso.move(0,-speed)
    
            
            fenetre.blit(perso, position_perso)
            pygame.display.flip()

        if  key[pygame.K_d] :
            clock.tick(time)                   #droite
            position_perso = position_perso.move(speed,0)
            for d in range (0,len(rekt_boîte)):
                if position_perso.colliderect(rekt_boîte[d]):
                    position_perso = position_perso.move(-repouser,0)
                
            if position_perso[0]<0:
                position_perso = position_perso.move(speed,0)
            if position_perso[0]>hauteur_x:
                position_perso = position_perso.move(-speed,0)
            if position_perso[1]<0:
                position_perso = position_perso.move(0,speed)
            if position_perso[1]>hauteur_y:
                position_perso = position_perso.move(0,-speed)


            fenetre.blit(perso, position_perso)
            pygame.display.flip()

        if  key[pygame.K_w] :
            clock.tick(time)                      # monter
            position_perso = position_perso.move(0,-speed)
            for d in range (0,len(rekt_boîte)):
                if position_perso.colliderect(rekt_boîte[d]):
                    position_perso = position_perso.move(0,repouser)
                
            if position_perso[0]<0:
                position_perso = position_perso.move(speed,0)
            if position_perso[0]>hauteur_x:
                position_perso = position_perso.move(-speed,0)
            if position_perso[1]<0:
                position_perso = position_perso.move(0,speed)
            if position_perso[1]>hauteur_y:
                position_perso = position_perso.move(0,-speed)


            fenetre.blit(perso, position_perso)
            pygame.display.flip()

        if  key[pygame.K_s] :
            clock.tick(time)  
                                                  #décendre
            position_perso = position_perso.move(0,speed)
            for d in range (0,len(rekt_boîte)):                                           
                if position_perso.colliderect(rekt_boîte[d]):
                    position_perso = position_perso.move(0,-repouser)
                
            if position_perso[0]<0:
                position_perso = position_perso.move(speed,0)
            if position_perso[0]>hauteur_x:
                position_perso = position_perso.move(-speed,0)
            if position_perso[1]<0:
                position_perso = position_perso.move(0,speed)
            if position_perso[1]>hauteur_y:
                position_perso = position_perso.move(0,-speed)
            
            fenetre.blit(perso,position_perso)
            pygame.display.flip()


            pygame.display.flip()


