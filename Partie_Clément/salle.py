import pygame
from pygame.locals import *

def salle():
    from random import randrange
    from pos_boîte import position_boîte

    position_x_y = position_boîte()
    caisses=len (position_x_y)


    pygame.init()
    fenetre = pygame.display.set_mode((1145,720))


    table = pygame.image.load("images/salle.png").convert()
    fenetre.blit(table, (0,0))

    perso = pygame.image.load("images/perso.jpg").convert()                         # !!! à voir ...
    fenetre.blit(perso, (30,30))

    caisse = pygame.image.load("images/boîte.jpg").convert()
    pygame.display.flip()

    for i in range (0,caisses):
        b=position_x_y[i]
        x= b[0]
        y= b[1]
        fenetre.blit(caisse, (x,y))

    pygame.display.flip()



salle()



