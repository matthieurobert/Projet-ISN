import pygame
import time
from pygame.locals import*

pygame.init()

#affichage de la fenêtre
fen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Chrono")

blue = (255, 255, 255)
black = (0, 0, 0)
rouge = (255,25,0)

temps = int(time.time())
continuer1 = 1
continuer2 = 2

while continuer1:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer1 = 0
            continuer2 = 0


        if evenement.type == KEYDOWN:
            if evenement.key == K_s:
                continuer1 = 0

    depart=time.time()
    conteur =int(depart-temps)
    time.sleep(1)
    chiffre=str(conteur)
    myrect = pygame.Rect(10,10, 150, 30)
    pygame.draw.rect(fen, black, myrect)

    arial_font = pygame.font.SysFont("arial",30)

    hello_texte_surface = arial_font.render("Score : "+chiffre, True, blue)
    fen.blit(hello_texte_surface,(10,10))



    pygame.display.flip()
conteur = conteur - 2
while continuer2:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:

            continuer2 = 0

            pygame.display.quit()
    carre_noir = pygame.Rect(10,10, 150, 30)
    pygame.draw.rect(fen, black, carre_noir)
    
    score_finale=str(conteur)
    hello_texte_surface = arial_font.render("Score : "+score_finale, True, blue)

    perso = pygame.image.load("gameover.jpg")

    fen.blit(perso, (10,10))
    fen.blit(hello_texte_surface,(435,500))

    pygame.font.init()
    pygame.display.flip()



pygame.quit()