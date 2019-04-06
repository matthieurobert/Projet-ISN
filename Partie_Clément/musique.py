import pygame
from pygame.locals import *

#Initialisation
pygame.init()
fenetre = pygame.display.set_mode((300,300))
son = pygame.mixer.Sound("C:\\Users\\Clément\\Documents\\GitHub\\Projet-ISN\\Partie_Clément\\musique_fond\\tir.wav")

continuer = 1 #Variable de boucle
joue = 0 #1 si le son a été mis en pause
pygame.display.flip()
while continuer:

    for event in pygame.event.get():
        son.play(loops=-1, maxtime=0,fade_ms=0)



        if event.type == QUIT:

            pygame.quit()
    cleanup()