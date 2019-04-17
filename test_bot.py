import pygame
import sys
import time
from pygame.locals import *
from Partie_Clément.rekt_boîte import rekt
from partie_lilian.fonction import murs_colision,game_over,vie_coeur,chrono,gauche,droite,monter,decendre

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

perso = pygame.image.load("perso.jpg").convert()
position_perso = perso.get_rect()

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

class Pojectiles(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Test_Matthieu/projectiles.png")
        self.rect = position_perso
        self.posinit = position_perso
        self.alive = 1

    def droite(self):
        self.rect = self.rect.move(2,0)
        for d in range (0, len(rekt_boîte)):
            if self.rect.colliderect(rekt_boîte[d]):
                self.alive = 0
                self.kill()
    
    def gauche(self): 
        self.rect = self.rect.move(-2,0)
        for d in range (0, len(rekt_boîte)):
            if self.rect.colliderect(rekt_boîte[d]):
                self.alive = 0 
                self.kill()
    
    def haut(self):
        self.rect = self.rect.move(0, -2)
        for d in range (0, len(rekt_boîte)):
            if self.rect.colliderect(rekt_boîte[d]):
                self.alive = 0
                self.kill()

    def bas(self):
        self.rect = self.rect.move(0, 2)
        for d in range (0, len(rekt_boîte)):
            if self.rect.colliderect(rekt_boîte[d]):
                self.alive = 0
                self.kill()


class FolBot(pygame.sprite.Sprite):



	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Test_Matthieu/sprite2.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect = pygame.Rect(400,200,50,50)
		#self.side = side
		#self.speed = 10
		self.state = "still"
	
		

	def bas(self):
		self.rect = self.rect.move(0, 1)

	def haut(self):
		self.rect = self.rect.move(0, -1)
	
	def gauche(self):
		self.rect = self.rect.move(-1, 0)

	def droite(self):
		self.rect = self.rect.move(1, 0)


black = (0, 0, 0)
rouge = (255,25,0)
white = (255,255,255)
depart = int(time.time())
temps = time.time()
conteur =int(temps-depart)
chiffre=str(conteur)
arial_font = pygame.font.SysFont("arial",30)
point_vie = 3
image_coeur1 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
image_coeur2 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
image_coeur3 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
image_coeur4 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
image_coeur5 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()   
speed =4
repouser = speed
aff_crono = arial_font.render("Score : "+chiffre, True, black)
ips = 60
hauteur_x = 1100
hauteur_y= 675
clock = pygame.time.Clock()
pygame.display.flip() 
alien = ARBot()
pab = LRBot()
follower = FolBot()
balle = Pojectiles()

pygame.display.flip

continuer = 1
continuer2 = 1
continuer3 = 1
pygame.key.set_repeat(50,15)
while continuer :
    while continuer2:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                pygame.quit()

        if abs(position_perso[0] - follower.rect[0]) == abs(position_perso[1] - follower.rect[1]):
            if abs(position_perso[0] - follower.rect[0]) != position_perso[0] - follower.rect[0]:
                follower.gauche()
            else:
                follower.droite()
        elif abs(position_perso[0] - follower.rect[0]) > abs(position_perso[1] - follower.rect[1]):
            if abs(position_perso[0]-follower.rect[0]) != position_perso[0] - follower.rect[0]:
                follower.gauche()
            else:
                follower.droite()
        elif abs(position_perso[0] - follower.rect[0]) < abs(position_perso[1] - follower.rect[1]):
            if abs(position_perso[1]-follower.rect[1]) != position_perso[1] - follower.rect[1]:
                follower.haut()
            else:
                follower.bas()
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        fenetre.blit(table, (0, 0))
        for i in range (0,caisses):
           b=position_x_y[i]
           x= b[0]
           y= b[1]
           fenetre.blit(caisse, (x,y))
        vie_coeur(point_vie,fenetre,image_coeur1,image_coeur2,image_coeur3,image_coeur4,image_coeur5)

        fenetre.blit( alien.image, alien.rect)
        fenetre.blit( pab.image, pab.rect)
        fenetre.blit(perso,position_perso)
        fenetre.blit(aff_crono,(500,5))
        fenetre.blit( follower.image, follower.rect)
        if balle.alive :
            fenetre.blit( balle.image, balle.rect)
  
        pab.update()
        balle.droite()

        pygame.display.flip()


        aff_crono=chrono(depart,black)
    

        for event in pygame.event.get():
   
            if event.type == QUIT:
                continuer = 1
                pygame.quit()
            
            if  event.type == KEYDOWN :
                if event.key == K_a:
                    position_perso=gauche(position_perso,speed,rekt_boîte,repouser,fenetre,ips,clock,perso,murs_colision)
                    fenetre.blit(perso, position_perso)      #gauche
                    pygame.display.flip()
                if event.key == K_d:
                    position_perso=droite(position_perso,speed,rekt_boîte,repouser,fenetre,ips,clock,perso,murs_colision)
                    fenetre.blit(perso, position_perso)        #droite     
                    pygame.display.flip()

                if event.key == K_w:
                    position_perso=monter(position_perso,speed,rekt_boîte,repouser,fenetre,ips,clock,perso,murs_colision)
                    fenetre.blit(perso, position_perso)             
                    pygame.display.flip()                       #monter

                if event.key == K_s:
                    position_perso=decendre(position_perso,speed,rekt_boîte,repouser,fenetre,ips,clock,perso,murs_colision)
                    fenetre.blit(perso,position_perso)           #decendre
                    pygame.display.flip()


                    pygame.display.flip()
                
                if event.key == K_v : 
                    point_vie = point_vie - 1
                if point_vie == 0 :
                    continuer2 = 0
    game_over(conteur,arial_font,fenetre,black)
    
    while continuer3:
        for evenement in pygame.event.get():
            if evenement.type == QUIT:

                continuer3 = 0
                pygame.display.quit()
            if event.key == KEYDOWN:
                if event.key == K_r:
                    continuer3 = 0
                    continuer2 = 1    
      
        pygame.display.flip()
        pygame.font.init()



pygame.quit()