import pygame
from pygame.locals import *
def sound():
    son = pygame.mixer.Sound('perdu.wav')
    son.play()
sound()
