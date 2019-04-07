
import pygame
from pygame.locals import *
def deplacement():
    pygame.init()
    fenetre = pygame.display.set_mode((750,500))
    fond = pygame.image.load("background.jpg").convert()
    fenetre.blit(fond, (0,0))
    perso = pygame.image.load("perso.jpg").convert()
    x=10
    y=10
    speed = 20
    speed_diagonal = speed/2
    time = 80
    fenetre.blit(perso, (x,y))
    clock = pygame.time.Clock()
    pygame.display.flip()
    continuer = 0
    pygame.key.set_repeat(25,20)
    while continuer == 0:
        clock.tick(time)
        for event in pygame.event.get():
            key=pygame.key.get_pressed()
            

            if event.type == QUIT:
                continuer = 1
                pygame.quit()
            if  key[pygame.K_a] :
                clock.tick(time)             # gauche
                fenetre.blit(fond, (0,0))
                x = x-speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_d] :
                clock.tick(time)                   #droite
                fenetre.blit(fond, (0,0))
                x = x+speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_w] :
                clock.tick(time)                      # monter
                fenetre.blit(fond, (0,0))
                y = y-speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_s] :
                clock.tick(time)                     #décendre
                fenetre.blit(fond, (0,0))
                y = y+speed
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_s] and key[pygame.K_a]   :
                clock.tick(time)
                fenetre.blit(fond, (0,0))
                y = y+speed_diagonal
                x=x-speed_diagonal
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_s] and key[pygame.K_d] :
                clock.tick(time)
                fenetre.blit(fond, (0,0))
                y = y+speed_diagonal
                x= x+speed_diagonal
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_w] and key[pygame.K_d] :
                clock.tick(time)
                fenetre.blit(fond, (0,0))
                y = y-speed_diagonal
                x=x+speed_diagonal
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_w] and key[pygame.K_a] :
                clock.tick(time)
                fenetre.blit(fond, (0,0))
                y = y-speed_diagonal
                x=x-speed_diagonal
                fenetre.blit(perso, (x,y))
                pygame.display.flip()
deplacement()
