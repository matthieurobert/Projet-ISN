import pygame
from pygame.locals import *

def salle():                                                                     # création de la fonction salle
    from random import randrange
    from Partie_Clément.pos_boîte import position_boîte



    position_x_y = position_boîte()
    caisses=len (position_x_y)


    pygame.init()
    fenetre = pygame.display.set_mode((1145,720))                                # initialisation de pygame et de la fenêtre


    table = pygame.image.load("Test_Matthieu/map.png").convert()       # on affiche le fond
    fenetre.blit(table, (0,0))



    caisse = pygame.image.load("Partie_Clément/images/boîte.jpg").convert()      # on importe l'image caisse
    pygame.display.flip()

    for i in range (0,caisses):                                                  # pour chaque coordonnées on affiche la boîte
        b=position_x_y[i]
        x= b[0]
        y= b[1]
        fenetre.blit(caisse, (x,y))

    pygame.display.flip()

    liste = [fenetre, table, caisse, caisses, position_x_y]

    return (liste)

"""   on renvoie la valeur liste contenant :
                                            -la fenêtre
                                            -l'image de fond
                                            -l'image de la caisse
                                            -le nombre de caisses
                                            -position_x_y des caisses """







