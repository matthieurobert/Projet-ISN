import pygame
from pygame.locals import *
def murs_colision(speed,position_perso) :
    hauteur_x = 1100
    hauteur_y= 675
    if position_perso[0]<0:
        position_perso = position_perso.move(speed,0)
    if position_perso[0]>hauteur_x:
        position_perso = position_perso.move(-speed,0)
    if position_perso[1]<0:
        position_perso = position_perso.move(0,speed)
    if position_perso[1]>hauteur_y:
        position_perso = position_perso.move(0,-speed)
    return position_perso

def game_over(chiffre) :
    black = (0,0,0)
    arial_font = pygame.font.SysFont("arial",30)
    afichage_score_final = arial_font.render("Score : "+chiffre, True, black)

    image_game_over = pygame.image.load("partie_lilian\gameover.jpg").convert_alpha()
    information_game_over = [afichage_score_final,image_game_over]
    return information_game_over
    