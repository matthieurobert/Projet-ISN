import pygame
from pygame.locals import *
import time
def variable():
    black = (0, 0, 0)
    rouge = (255,25,0)
    white = (255,255,255)
    depart = int(time.time())
    temps = time.time()
    conteur =int(temps-depart)
    chiffre=str(conteur)
    arial_font = pygame.font.SysFont("arial",30)
    point_vie = 3
    image_coeur1 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
    image_coeur2 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
    image_coeur3 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
    image_coeur4 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
    image_coeur5 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()   
    speed =4
    repouser = speed
    aff_crono = arial_font.render("Score : "+chiffre, True, black)
    ips = 60
    hauteur_x = 1100
    hauteur_y= 675
    variable[0] = black
    variable[1] = rouge
    variable[2] = white
    variable[3] = depart
    variable[4] = temps
    variable[5] = conteur
    variable[6] = chiffre
    variable[7] = arial_font
    variable[8] = point_vie
    variable[9] = image_coeur1
    variable[10] = image_coeur2
    variable[11] = image_coeur3
    variable[12] = image_coeur4
    variable[13] = image_coeur5
    variable[14] = speed
    variable[15] = repouser
    variable[16] = ips
    variable[17] = hauteur_x
    variable[18] = hauteur_y
    variable[19] = aff_crono
    return(variable)
   