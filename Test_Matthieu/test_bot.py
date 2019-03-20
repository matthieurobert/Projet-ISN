import pygame 
from pygame.locals import *

pygame.init()


class ARBot(pygame.sprite.Sprite):
	
	

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("sprite.png")
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect = self.image.get_rect()
		#self.side = side
		#self.speed = 10
		self.state = "still"
		self.newpos = [0, 0]
		self.speed = [0, 5]
		self.update()

	#def reinit(self):
		#self.state = "still"
		#self.movepos = [0, 5]
	
	def update(self):
		if self.rect.top < 0:
			self.newpos[1] = self.newpos[1] + self.speed[1]
			self.rect = self.rect.move(self.newpos)
		#if self.area.contains(self.newpos):
		elif self.rect.bottom > 440:
			self.newpos[1] = self.newpos[1] - self.speed[1]
			self.rect = self.rect.move(self.newpos)
		
		else:
			self.newpos[1] = self.newpos[1] + self.speed[1]
			self.rect = self.rect.move(self.newpos)
		
		print(self.speed)
		

		

	#def moveup(self):
		#self.movepos[1] = self.movepos[1] - (self.speed)
		#self.state = "moveup"
		
	#def movedown(self):
		#self.movepos[1] = self.movepos[1] + (self.speed)
		#self.state = "movedown"



speed = [0, 5]

fenetre = pygame.display.set_mode((600,640), RESIZABLE)

fond = pygame.image.load("background.png")
fenetre.blit(fond, (0 , 0))

#player = pygame.image.load("sprite.png")
#pos_player  = player.get_rect()
#fenetre.blit(player, pos_player)

alien = ARBot()

pygame.display.flip

continuer = 1 

while continuer:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	
	#alien.update()
	fenetre.blit(fond, (0, 0))
	fenetre.blit( alien.image, alien.rect)
	alien.update()
	pygame.display.flip()

		
		