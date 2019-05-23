import pygame
from pygame.locals import *

from test_bot import fonction_principal
pygame.init()
continue1 = 1
continue2 = 1
while continue1 :
    continue2 = 1
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer1 = 0
            pygame.quit()
    while continue2 : 
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer1 = 0
                continuer2 = 0
                pygame.quit()
        continue2 = fonction_principal()