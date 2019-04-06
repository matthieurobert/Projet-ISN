import pygame
import time
from pygame.locals import*

pygame.init()

#affichage de la fenêtre




class Bat(pygame.sprite.Sprite):
    
    def __init__(self, side):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('perso.jpg')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 10
        self.state = "still"
        self.reinit()

    def reinit(self):
        self.state = "still"
        self.movepos = [0,0]
        if self.side == "left":
            self.rect.midleft = self.area.midleft
        elif self.side == "right":
            self.rect.midright = self.area.midright

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveup(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = "moveup"

    def movedown(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = "movedown"
font = pygame.display.set_mode((1000, 600))

fond = pygame.image.load("background.jpg").convert()
continuer1 = 1

player = Bat()


while continuer1:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer1 = 0
        elif evenement.type == KEYDOWN:
            if evenement.key == K_UP:
                player.moveup()
            if evenement.key == K_DOWN:
        	    player.movedown()
        elif evenement.type == KEYUP:
      	  if evenement.key == K_UP or event.key == K_DOWN:
          		player.movepos = [0,0]
                

    pygame.font.init()
    pygame.display.flip()


pygame.quit()