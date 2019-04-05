import pygame
from pygame.locals import *

#Initialisation
pygame.init()
fenetre = pygame.display.set_mode((300,300))
son = pygame.mixer.Sound("C:\\Users\\Clément\\Documents\\GitHub\\Projet-ISN\\Partie_Clément\\musique_fond\\Ozzed_-_World_Nap_REMIX.wav")

continuer = 1 #Variable de boucle
joue = 0 #1 si le son a été mis en pause

while continuer:
    son.play()
    continuer = int(input())
    if continuer == 0 :
        pygame.quit()
