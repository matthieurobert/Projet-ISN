import pygame
import sys
import time
from pygame.locals import *
from Partie_Clément.rekt_boîte import rekt
from partie_lilian.fonction import murs_colision,game_over


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
        self.rect = pygame.Rect(0,500, 20, 20)
        self.posinit = pygame.Rect(0,500,20,20)
        self.speed = [1,0]
        self.update()

    def update(self):
        self.rect = self.rect.move(self.speed)
        for d in range (0, len(rekt_boîte)):
            if self.rect.colliderect(rekt_boîte[d]):
                self.kill()
                self.speed[0] = 0
        

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

class projecctil(pygame.sprite.Sprite):



	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("partie_lilian/projectile.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect = pygame.Rect(0,200,50,50)
		#self.side = side
		#self.speed = 10
		self.state = "still"
		self.newpos = [0, 0]
		
		self.update()


	def droite(self):
        self.speed = [1,0]
		if self.rect.left < 0 or self.rect.right > 1095:
			self.speed[0] = -self.speed[0]

		for d in range (0,len(rekt_boîte)):

			if self.rect.colliderect(rekt_boîte[d]):
				self.speed[0] = -self.speed[0]

		self.rect = self.rect.move(self.speed)





black = (0, 0, 0)
rouge = (255,25,0)
white = (255,255,255)
depart = int(time.time())
temps = time.time()
conteur =int(temps-depart)
chiffre=str(conteur)
myrect = pygame.Rect(10,10, 150, 30)
arial_font = pygame.font.SysFont("arial",30)
hello_texte_surface = arial_font.render("Score : "+chiffre, True, black)


image_coeur1 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
image_coeur2 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
image_coeur3 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
image_coeur4 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
image_coeur5 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
point_vie = 5
chaine_vie = str(point_vie)
image_vie = arial_font.render(" x "+chaine_vie,True, black)


speed =4
repouser = speed
speed_diagonal = speed/2
ips = 60
hauteur_x = 1100
hauteur_y= 675

clock = pygame.time.Clock()
pygame.display.flip()
continuer = 0
pygame.key.set_repeat(50,15)

alien = ARBot()
pab = LRBot()
follower = FolBot()
balle = Pojectiles()

pygame.display.flip
continuer = 1
continuer2 = 1
continuer3 = 1
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
        if point_vie>=1:
            fenetre.blit(image_coeur1,(934,8))
            if point_vie>=2:
                fenetre.blit(image_coeur2,(972,8))
                if point_vie>=3:
                    fenetre.blit(image_coeur3,(1010,8))
                    if point_vie>=4:
                        fenetre.blit(image_coeur4,(1045,8))
                        if point_vie>=5:
                            fenetre.blit(image_coeur5,(1080,8))

        fenetre.blit( alien.image, alien.rect)
        fenetre.blit( pab.image, pab.rect)
        fenetre.blit(perso,position_perso)
        fenetre.blit(hello_texte_surface,(500,5))
        fenetre.blit( follower.image, follower.rect)
        fenetre.blit( balle.image, balle.rect)
  
        pab.update()
        balle.update()

        pygame.display.flip()


        temps = time.time()
        conteur =int(temps-depart)
        chiffre=str(conteur)
        myrect = pygame.Rect(10,10, 150, 30)
    

        arial_font = pygame.font.SysFont("arial",30)

        hello_texte_surface = arial_font.render("Score : "+chiffre, True, black)
    

        for event in pygame.event.get():
   
            if event.type == QUIT:
                continuer = 1
                pygame.quit()
            
            if  event.type == KEYDOWN :
                if event.key == K_a:
                    clock.tick(ips)             # gauche
                    position_perso = position_perso.move(-speed,0)
                    for d in range (0,len(rekt_boîte)):
                        if position_perso.colliderect(rekt_boîte[d]):
                            position_perso = position_perso.move(repouser,0)
            
                    position_perso = murs_colision(speed,position_perso)   
            
                    fenetre.blit(perso, position_perso)           
                    pygame.display.flip()

                if event.key == K_d:
                    clock.tick(ips)                   #droite
                    position_perso = position_perso.move(speed,0)
                    for d in range (0,len(rekt_boîte)):
                        if position_perso.colliderect(rekt_boîte[d]):
                            position_perso = position_perso.move(-repouser,0)
                
                    position_perso = murs_colision(speed,position_perso) 


                    fenetre.blit(perso, position_perso)             
                    pygame.display.flip()

                if event.key == K_w:
                    clock.tick(ips)                      # monter
                    position_perso = position_perso.move(0,-speed)
                    for d in range (0,len(rekt_boîte)):
                        if position_perso.colliderect(rekt_boîte[d]):
                            position_perso = position_perso.move(0,repouser)
               
                    position_perso = murs_colision(speed,position_perso) 

                    fenetre.blit(perso, position_perso)             
                    pygame.display.flip()

                if event.key == K_s:
                    clock.tick(ips)  
                                                  #décendre
                    position_perso = position_perso.move(0,speed)
                    for d in range (0,len(rekt_boîte)):                                           
                        if position_perso.colliderect(rekt_boîte[d]):
                            position_perso = position_perso.move(0,-repouser)
               
                    position_perso = murs_colision(speed,position_perso) 
            
                    fenetre.blit(perso,position_perso)           
                    pygame.display.flip()


                    pygame.display.flip()
                
                if event.key == K_v : 
                    point_vie = point_vie - 1
                if point_vie == 0 :
                    continuer2 = 0
    score_finale=str(conteur)
    aff_score_final = arial_font.render("Score : "+score_finale, True, black)
    fenetre.blit(aff_score_final,(500,550))
    affi_gam_over = pygame.image.load("partie_lilian\gameover.jpg").convert_alpha()

    fenetre.blit(affi_gam_over,(125,5))
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