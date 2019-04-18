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
   speed =4
   repouser = speed
   aff_crono = arial_font.render("Score : "+chiffre, True, black)
   ips = 60
   hauteur_x = 1100
   hauteur_y= 675
   clock = pygame.time.Clock()
   variable=[black,rouge,white,depart,temps,conteur,chiffre,arial_font,point_vie,speed,repouser,ips,hauteur_x,hauteur_y,aff_crono]

   return(variable)
"""
les_variable = variable()
black = les_variable[0]
rouge = les_variable[1]
white = les_variable[2]
depart = les_variable[3]
temps = les_variable[4]
conteur = les_variable[5]
chiffre = les_variable[6]
arial_font = les_variable[7]
point_vie = les_variable[8]
speed = les_variable[9]
repouser = les_variable[10]
ips = les_variable[11]
hauteur_x = les_variable[12]
hauteur_y = les_variable[13]
aff_crono = les_variable[14]
"""