import pygame
from pygame.locals import *

def salle():
    from random import randrange

    pygame.init()
    fenetre = pygame.display.set_mode((1145,720))


    table = pygame.image.load("images/salle.png").convert()                   # on importe l'image "blackjack_table.png"
    fenetre.blit(table, (0,0))

    perso = pygame.image.load("images/perso.jpg").convert()
    fenetre.blit(perso, (575,360))

    pygame.display.flip()

    nombre_obstacle = randrange(5,15)

    spé_caisse = randrange(1,4)


    for i in range(0,nombre_obstacle):

        obstacle = pygame.image.load("images/boîte.jpg").convert_alpha()
        x=randrange(100,1000)
        y=randrange(100,600)

        fenetre.blit(obstacle, (x,y))


    for i in range(0,spé_caisse):
        pouvoirs = pygame.image.load("images/boite_mystere.jpg").convert_alpha()
        x=randrange(100,1000)
        y=randrange(100,600)

        fenetre.blit(pouvoirs, (x,y))
    pygame.display.flip()





salle()