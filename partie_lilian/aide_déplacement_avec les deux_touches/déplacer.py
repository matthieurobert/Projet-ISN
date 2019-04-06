import pygame
from pygame.locals import *
def sound():
    pygame.init()
    fenetre = pygame.display.set_mode((640,480))
    fond = pygame.image.load("background.jpg").convert()
    fenetre.blit(fond, (0,0))
    perso = pygame.image.load("perso.png").convert_alpha()
    x=600
    y=0
    fenetre.blit(perso, (x,y))
    pygame.display.flip()
    clock = pygame.time.Clock()


    continuer = 1 #Variable de boucle
    joue = 0 #1 si le son a été mis en pause


    pygame.key.set_repeat(1,20)
    while continuer:
        clock.tick(30)
        for event in pygame.event.get():
            key=pygame.key.get_pressed()


            if event.type == QUIT:
                continuer = 0
                pygame.quit()

            if  key[pygame.K_DOWN] and key[pygame.K_LEFT]   :


                clock.tick(10)
                fenetre.blit(fond, (0,0))
                y = y+10
                x=x-10
                fenetre.blit(perso, (x,y))
                pygame.display.flip()

sound()
