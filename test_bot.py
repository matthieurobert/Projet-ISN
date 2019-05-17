import pygame
import sys
import time
from pygame.locals import *
from Partie_Clément.rekt_boîte import rekt
from Partie_Clément.liste_x_y_bot import liste
from partie_lilian.fonction import murs_colision,game_over,vie_coeur,chrono,gauche,droite,monter,decendre,demande_de_nom
from partie_lilian.variable import variable
from random import randrange
from Partie_Clément.musique import musique_blesse
from Partie_Clément.musique import musique_tir
from Partie_Clément.musique import musique_fin
from Partie_Clément.musique import musique_fond


pygame.init()
nom_joueur=str
nom_joueur = demande_de_nom()

bot_x_y = liste()
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

class TBBot(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Test_Matthieu/sprite2.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect = pygame.Rect(0,400,50,50)
		self.speed = [0,1]
		self.update()


	def update(self):
		if self.rect.top < 0 or self.rect.bottom > 680:
			self.speed[1] = -self.speed[1]

		for d in range (0,len(rekt_boîte)):

			if self.rect.colliderect(rekt_boîte[d]):
				self.speed[1] = -self.speed[1]

		self.rect = self.rect.move(self.speed)

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

class RBot(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Test_Matthieu/sprite.png")
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect = pygame.Rect(0,500,50,50)
        self.speed = [1, 0]
        self.update()


    def update(self):
        if self.rect.left < 0 or self.rect.right > 1095:
            if self.speed == [1,0]:
                self.speed = [0,1]
            elif self.speed == [0,1]:
                self.speed = [-1,0]
            elif self.speed == [-1,0]:
                self.speed = [0,-1]
            elif self.speed == [0,-1]:
                self.speed = [1,0]

        for d in range (0,len(rekt_boîte)):

            if self.rect.colliderect(rekt_boîte[d]):
                if self.speed == [1,0]:
                    self.speed = [0,1]
                elif self.speed == [0,1]:
                    self.speed = [-1,0]
                elif self.speed == [-1,0]:
                    self.speed = [0,-1]
                elif self.speed == [0,-1]:
                    self.speed = [1,0]

        self.rect = self.rect.move(self.speed)

class Pojectiles(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Test_Matthieu/projectiles.png")
        self.rect = position_perso
        self.posinit = position_perso
        self.alive = 1

    def droite(self):
        self.rect = self.rect.move(4,0)
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
		self.image = pygame.image.load("Test_Matthieu/sprite4.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect = pygame.Rect(400,200,50,50)
		#self.side = side
		#self.speed = 10
		self.state = "still"
		self.n = 0



	def bas(self):
		if self.n % 500 == 0:
			self.rect = self.rect.move(0, 5)
			self.n = self.n + 1
		else:
			self.rect = self.rect.move(0,1)
			self.n = self.n + 1
	def haut(self):
		if self.n % 500 == 0:
			self.rect = self.rect.move(0, -5)
			self.n = self.n + 1
		else:
			self.rect = self.rect.move(0,-1)
			self.n = self.n + 1
	def gauche(self):
		if self.n % 500 == 0:
			self.rect = self.rect.move(-5, 0)
			self.n = self.n + 1
		else:
			self.rect = self.rect.move(-1,0)
			self.n = self.n + 1
	def droite(self):
		if self.n % 500 == 0:
			self.rect = self.rect.move(5, 0)
			self.n = self.n + 1
		else:
			self.rect = self.rect.move(1,0)
			self.n = self.n + 1
	def stop(self):
		self.rect = self.rect.move(0,0)

les_variable = variable()
black = les_variable[0]
rouge = les_variable[1]
white = les_variable[2]
depart = les_variable[3]
temps = les_variable[4]
conteur = les_variable[5]
chiffre = les_variable[6]
arial_font = les_variable[7]
point_vie = les_variable[8]
speed = les_variable[9]
repouser = les_variable[10]
ips = les_variable[11]
hauteur_x = les_variable[12]
hauteur_y = les_variable[13]
aff_crono = les_variable[14]

bots = pygame.sprite.Group()

clock = pygame.time.Clock()
pygame.display.flip()
bot = TBBot()
pab = LRBot()
copybot = pygame.sprite.Group.copy
follower = FolBot()
balle = Pojectiles()
ran = RBot()


bots.add(bot)
bots.add(pab)
bots.add(follower)
bots.add(ran)

pygame.display.flip

continuer = 1
continuer2 = 1
continuer3 = 1
x = 1
musique_fond()
if x == 1:
    while continuer :

        pygame.key.set_repeat(50,15)
        while continuer2:

            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                    pygame.quit()
            if follower.rect.colliderect(position_perso):
                follower.stop()
                point_vie = point_vie - 1
                if point_vie != 0:
                    musique_blesse()
                rand = randrange(1,18)
                follower.rect= pygame.Rect(bot_x_y[rand])
                pab.rect= pygame.Rect(bot_x_y[rand+1])
                fenetre.blit( follower.image,follower.rect)
                fenetre.blit( pab.image, pab.rect)
            elif abs(position_perso[0] - follower.rect[0]) == abs(position_perso[1] - follower.rect[1]):
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

            if pab.rect.colliderect(position_perso):
                point_vie = point_vie - 1
                if point_vie != 0:
                    musique_blesse()
                rand = randrange(1,18)
                follower.rect= pygame.Rect(bot_x_y[rand])
                pab.rect= pygame.Rect(bot_x_y[rand+1])
                fenetre.blit( follower.image,follower.rect)
                fenetre.blit( pab.image, pab.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


            fenetre.blit(table, (0, 0))
            for i in range (0,caisses):
               b=position_x_y[i]
               x= b[0]
               y= b[1]
               fenetre.blit(caisse, (x,y))
            vie_coeur(point_vie,fenetre)

            fenetre.blit(copybot.image , copybot.rect)
            fenetre.blit( pab.image, pab.rect)
            fenetre.blit( bot.image, bot.rect)
            fenetre.blit( ran.image, ran.rect)
            fenetre.blit(perso,position_perso)
            fenetre.blit(aff_crono,(500,5))
            fenetre.blit( follower.image, follower.rect)
            # Projectile
            if balle.alive :
                fenetre.blit( balle.image, balle.rect)
            copybot.update()
            pab.update()
            bot.update()
            ran.update()
            balle.droite()
            follower.update()
            pygame.display.flip()

            liste_crono=chrono(depart,black)
            aff_crono = liste_crono[0]
            conteur = liste_crono[1]


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
                        musique_blesse()
                        r = randrange(1,18)
                        follower.rect= pygame.Rect(bot_x_y[r])
                        pab.rect= pygame.Rect(bot_x_y[r+1])
                        fenetre.blit( follower.image,follower.rect)
                        fenetre.blit( pab.image, pab.rect)
                        pygame.display.flip()
            if point_vie == 0 :
                continuer2 = 0
                continuer3 = 1


        game_over(conteur,fenetre,nom_joueur)
        musique_fin()
        while continuer3:
            for event in pygame.event.get():
                if event.type == QUIT:

                    continuer3 = 0
                    pygame.display.quit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        point_vie = 3
                        continuer2 = 1
                        continuer3=0
                        fenetre.blit(perso,(0,0))
                        pygame.display.flip()
                        musique_fond()



            pygame.display.flip()
            pygame.font.init()
