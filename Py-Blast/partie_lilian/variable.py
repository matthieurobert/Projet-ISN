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
   speed =8
   repouser = speed
   aff_crono = arial_font.render("Score : "+chiffre, True, black)
   ips = 60
   hauteur_x = 1100
   hauteur_y= 675
   clock = pygame.time.Clock()
   variable=[black,rouge,white,depart,temps,conteur,chiffre,arial_font,point_vie,speed,repouser,ips,hauteur_x,hauteur_y,aff_crono]

   return(variable)
