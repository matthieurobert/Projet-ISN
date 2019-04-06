import pygame 
import sys
from pygame.locals import *
from Partie_Clément.salle import salle
from Partie_Clément.rekt_boîte import rekt

pygame.init()

liste = salle()
rekt_boîte = rekt()
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
		if self.rect.top < 0:
			self.newpos[1] = self.newpos[1] + self.speed[1]
			self.rect = self.rect.move(self.newpos)
		
		elif self.rect.bottom > 670:
			self.newpos[1] = self.newpos[1] - self.speed[1]
			self.rect = self.rect.move(self.newpos)
		
		else:
			self.newpos[1] = self.newpos[1] + self.speed[1]
			self.rect = self.rect.move(self.newpos)
		
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
		

		if self.rect.left < 0 :
			self.newpos[0] = self.newpos[0] + self.speed[0]
			self.rect = self.rect.move(self.newpos)
		
		elif self.rect.right > 1095:
			self.newpos[0] = self.newpos[0] - self.speed[0]
			self.rect = self.rect.move(self.newpos)
		
		elif self.rect.collidelist(rekt_boîte):
			self.newpos[0] = self.newpos[0] - self.speed[0]
			self.rect = self.rect.move(self.newpos)
		
		else:
			self.newpos[0] = self.newpos[0] + self.speed[0]
			self.rect = self.rect.move(self.newpos)
		
		#print(self.speed)


alien = ARBot()
pab = LRBot()

pygame.display.flip

continuer = 1 

while continuer:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	
	#alien.update()
	fenetre.blit(table, (0, 0))
	for i in range (0,caisses):
		b=position_x_y[i]
		x= b[0]
		y= b[1]
		fenetre.blit(caisse, (x,y))

	fenetre.blit( alien.image, alien.rect)
	fenetre.blit( pab.image, pab.rect)
	
	pab.update()
	
	pygame.display.flip()

		
		