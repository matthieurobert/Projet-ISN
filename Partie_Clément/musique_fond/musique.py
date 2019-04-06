import pygame
from pygame.locals import *
def sound():
    pygame.init()
    fenetre = pygame.display.set_mode((300,300))
    son = pygame.mixer.Sound("tir.wav")

    continuer = 1 #Variable de boucle
    joue = 0 #1 si le son a été mis en pause

    while continuer:
        for event in pygame.event.get():
                		#Lancer le son
            if event.type == KEYDOWN and event.key == K_SPACE and joue == 0:
                son.play(loops=0, maxtime=0, fade_ms=0)
                joue = 1
    		#Sortir de pause
            if event.type == KEYDOWN and event.key == K_SPACE and joue == 1:
                son.play(loops=0, maxtime=0, fade_ms=0)
                pygame.mixer.unpause()
    		#Mettre en pause
            if event.type == KEYUP and event.key == K_SPACE:
                pygame.mixer.pause()
    		#Stopper
            if event.type == QUIT:
                son.stop()
                continuer = 0
                pygame.quit()


sound()
