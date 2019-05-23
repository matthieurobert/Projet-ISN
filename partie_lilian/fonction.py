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

def game_over(conteur,fenetre,nom_joueur,mielleur_score) :
    blanc= (255,255,255)
    score_finale=str(conteur)
    nom_joueur=str(nom_joueur)
    Verdana_Pro_Black = pygame.font.SysFont('pygame.font.SysFont',25)
    arial = pygame.font.SysFont('Comic Sans MS,Arial', 45)
    aff_WR = Verdana_Pro_Black.render("WR : "+mielleur_score[1]+" par "+mielleur_score[0],True,blanc)
    aff_nom = arial.render(nom_joueur, True, blanc)
    aff_score_final = arial.render("Score : "+score_finale, True, blanc)
    affi_gam_over = pygame.image.load("partie_lilian\gameover-py-blast.jpg").convert_alpha()
    fenetre.blit(affi_gam_over,(0,0))
    fenetre.blit(aff_nom,(480,325))
    fenetre.blit(aff_WR,(900,20))
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


def lire_base_donner():

        import pickle
      
        score_trier = []
        liste_classer = []
        liste_final = []
        score_pseudo = []
        
        
        with open('score.txt','r') as text_perso:
                info_perso = text_perso.read()
                liste_depart = info_perso.split()
                
        for i in range (0,(len(liste_depart)),2) :
                        
                if i<((len(liste_depart))-1):
                        score_pseudo= [liste_depart[i],liste_depart[i+1]]
                score_trier.append(score_pseudo)
        liste_classer.append(score_trier[0])        
        for j in range (1,(len(score_trier)),1):
                dernier_liste_sclasser = int(len(liste_classer)-1)
                chiffre_comparais = int(score_trier[j][1])
                plus_grand_liste_classer = int(liste_classer[dernier_liste_sclasser][1])
                if (chiffre_comparais > plus_grand_liste_classer) :
                        liste_classer.append(score_trier[j])
        premier_score = liste_classer[(len(liste_classer)-1)]
        return(premier_score)

def save_score(conteur,nom_joueur):
    import pickle
  
    score_fait = str(conteur)

    with open('score.txt','a') as score:

        score.write(nom_joueur) 
        score.write(' ')
        score.write(score_fait)
        score.write('\n')
    
    score.close()