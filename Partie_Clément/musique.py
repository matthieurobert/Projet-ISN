import pygame
from pygame.locals import *

def musique_blesse():

    pygame.mixer.stop()
    tir = pygame.mixer.Sound(r"C:\Users\Clément\Documents\GitHub\Projet-ISN\Partie_Clément\musique_fond\\Meme_cri.wav")
    loops = 0
    tir.play(loops, maxtime=0,fade_ms=0)


def musique_tir():

    pygame.mixer.stop()
    tir = pygame.mixer.Sound(r"C:\\Users\\Clément\\Documents\\GitHub\\Projet-ISN\\Partie_Clément\\musique_fond\\tir.wav")
    loops = 0
    tir.play(loops, maxtime=0,fade_ms=0)

def musique_fin():

    pygame.mixer.stop()
    tir = pygame.mixer.Sound(r"C:\Users\Clément\Documents\GitHub\Projet-ISN\Partie_Clément\musique_fond\\perdu.wav")
    loops = 0
    tir.play(loops, maxtime=0,fade_ms=0)

def musique_fond():

    pygame.mixer.stop()
    tir = pygame.mixer.Sound(r"C:\Users\Clément\Documents\GitHub\Projet-ISN\Partie_Clément\musique_fond\\Ozzed_-_World_Nap.wav")
    loops = 0
    tir.play(loops, maxtime=0,fade_ms=0)