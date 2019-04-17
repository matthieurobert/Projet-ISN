import pygame
from pygame.locals import *
import time
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

def game_over(conteur,arial_font,fenetre,black) :

    score_finale=str(conteur)
    aff_score_final = arial_font.render("Score : "+score_finale, True, black)
    fenetre.blit(aff_score_final,(500,550))
    affi_gam_over = pygame.image.load("partie_lilian\gameover.jpg").convert_alpha()
    fenetre.blit(affi_gam_over,(125,5))
def vie_coeur(point_vie,fenetre) :
    image_coeur1 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
    image_coeur2 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
    image_coeur3 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
    image_coeur4 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha()
    image_coeur5 = pygame.image.load("partie_lilian\sprite_coeur_moyene.png").convert_alpha() 
    if point_vie>=1:
        fenetre.blit(image_coeur1,(934,8))
        if point_vie>=2:
            fenetre.blit(image_coeur2,(972,8))
            if point_vie>=3:
                fenetre.blit(image_coeur3,(1010,8))
                if point_vie>=4:
                    fenetre.blit(image_coeur4,(1045,8))
                    if point_vie>=5:
                        fenetre.blit(image_coeur5,(1080,8))

def gauche(position_perso,speed,rekt_boîte,repouser,fenetre,ips,clock,perso,murs_colision):
    clock.tick(ips)             # gauche
    position_perso = position_perso.move(-speed,0)
    for d in range (0,len(rekt_boîte)):
        if position_perso.colliderect(rekt_boîte[d]):
            position_perso = position_perso.move(repouser,0)
            
    position_perso = murs_colision(speed,position_perso)   
            
               
    
    return(position_perso)

def droite(position_perso,speed,rekt_boîte,repouser,fenetre,ips,clock,perso,murs_colision):
    clock.tick(ips)             # gauche
    position_perso = position_perso.move(speed,0)
    for d in range (0,len(rekt_boîte)):
        if position_perso.colliderect(rekt_boîte[d]):
            position_perso = position_perso.move(-repouser,0)          
    position_perso = murs_colision(speed,position_perso)     
    return(position_perso)    

def monter(position_perso,speed,rekt_boîte,repouser,fenetre,ips,clock,perso,murs_colision):
    clock.tick(ips)             # gauche
    position_perso = position_perso.move(0,-speed)
    for d in range (0,len(rekt_boîte)):
        if position_perso.colliderect(rekt_boîte[d]):
            position_perso = position_perso.move(0,speed)          
    position_perso = murs_colision(speed,position_perso)     
    return(position_perso)    

def decendre(position_perso,speed,rekt_boîte,repouser,fenetre,ips,clock,perso,murs_colision):
    clock.tick(ips)             # gauche
    position_perso = position_perso.move(0,speed)
    for d in range (0,len(rekt_boîte)):
        if position_perso.colliderect(rekt_boîte[d]):
            position_perso = position_perso.move(0,-speed)          
    position_perso = murs_colision(speed,position_perso)     
    return(position_perso)    

def chrono(depart,black):
    temps = time.time()
    conteur =int(temps-depart)
    chiffre=str(conteur)
    liste_crono = []
    arial_font = pygame.font.SysFont("arial",30)
    aff_crono = arial_font.render("Score : "+chiffre, True, black)
    liste_crono=[aff_crono,conteur]
    return (liste_crono)