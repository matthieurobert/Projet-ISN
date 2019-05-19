import pygame
from pygame.locals import *
import time
from random import randrange

def demande_de_nom():

    pygame.init()
    continuer = 1
    while continuer:
        fenetre = pygame.display.set_mode((1145,720))
        menu = pygame.image.load("partie_lilian\Main.png")
        fenetre.blit(menu,(0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and 300 <= event.pos[0] <= 800 and 330 <= event.pos[1] <= 450:
                    font = pygame.image.load("partie_lilian\Enter_pseudo.png").convert_alpha()
                    continuer = 0

    bleu = (40, 120, 230)
    vert = (40, 230, 120)
    noir = (0, 0, 0)
    rouge = (255, 0, 0)
    arial = pygame.font.SysFont('Comic Sans MS,Arial', 45)
    nom_joueur = ""
    aff_nom_joueur = arial.render(nom_joueur, True, rouge)
    fenetre.blit(font,(0,0))
    pygame.display.flip()
    continuer = 1

    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    continuer = 0

                if event.key == pygame.K_BACKSPACE:
                    nom_joueur = nom_joueur[:-1]
                else:
                    nom_joueur += event.unicode
                aff_nom_joueur = arial.render(nom_joueur, True, rouge)

        fenetre.blit(font,(0,0))
        fenetre.blit(aff_nom_joueur, (400,300))
        pygame.display.flip()
    nom_joueur = nom_joueur[:-1]
    return(nom_joueur)

def murs_colision(speed,position_perso) :
    hauteur_x = 1092
    hauteur_y= 655
    if position_perso[0]<1:
        position_perso = position_perso.move(speed,0)
    if position_perso[0]>hauteur_x:
        position_perso = position_perso.move(-speed,0)
    if position_perso[1]<12:
        position_perso = position_perso.move(0,speed)
    if position_perso[1]>hauteur_y:
        position_perso = position_perso.move(0,-speed)
    return position_perso

def game_over(conteur,fenetre,nom_joueur) :
    blanc= (255,255,255)
    score_finale=str(conteur)
    nom_joueur=str(nom_joueur)
    arial = pygame.font.SysFont('Comic Sans MS,Arial', 45)
    aff_nom = arial.render(nom_joueur, True, blanc)
    aff_score_final = arial.render("Score : "+score_finale, True, blanc)
    affi_gam_over = pygame.image.load("partie_lilian\gameover-py-blast.jpg").convert_alpha()
    fenetre.blit(affi_gam_over,(0,0))
    fenetre.blit(aff_nom,(480,325))
    fenetre.blit(aff_score_final,(450,375))


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


def generatrice_nom():
    nombre= randrange(0,26)
    lettre = ["a","b","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"]
    nombre2= randrange(0,9)
    mots=[]
    for i in range (0,nombre2):
        mots.append(lettre[nombre])
        nombre= randrange(0,26)
    s=''
    mots_aleatoire = s.join(mots)
    return (mots_aleatoire)
