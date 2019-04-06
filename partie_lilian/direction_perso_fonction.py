
import pygame
from pygame.locals import *
def deplacement():
    pygame.init()
    fenetre = pygame.display.set_mode((640,480))
    fond = pygame.image.load("background.jpg").convert()
    fenetre.blit(fond, (0,0))
    perso = pygame.image.load("perso.jpg").convert()
    x=0
    y=0
    speed = 3
    clock = pygame.time.Clock()
    fenetre.blit(perso, (x,y))
    pygame.display.flip()
    continuer = 0
    pygame.key.set_repeat(30,20)
    while continuer:

        for event in pygame.event.get():
            key=pygame.key.get_pressed()
            clock.tick(30)

            if event.type == QUIT:
                continuer = 1
                pygame.quit()
            if  key[pygame.K_A] :
                clock.tick(30)                    # gauche
                fenetre.blit(fond, (0,0))
                x = x-speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_D] :
                clock.tick(30)                    #droite
                fenetre.blit(fond, (0,0))
                x = x+speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_W] :
                clock.tick(30)                      # monter
                fenetre.blit(fond, (0,0))
                y = y-speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_S] :
                clock.tick(30)                       #décendre
                fenetre.blit(fond, (0,0))
                y = y+speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_S] and key[pygame.K_A]   :
                clock.tick(30)
                fenetre.blit(fond, (0,0))
                y = y+speed
                x=x-speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_S] and key[pygame.K_D] :
                clock.tick(30)
                fenetre.blit(fond, (0,0))
                y = y+speed
                x= x+speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_W] and key[pygame.K_D] :
                clock.tick(30)
                fenetre.blit(fond, (0,0))
                y = y-speed
                x=x+speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_W] and key[pygame.K_A] :
                clock.tick(30)
                fenetre.blit(fond, (0,0))
                y = y-speed
                x=x-speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()
deplacement()
