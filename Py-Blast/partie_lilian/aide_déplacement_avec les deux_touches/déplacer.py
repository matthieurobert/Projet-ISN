

# Voici le code j'espère que c'est assez cair ...


import pygame
from pygame.locals import *
def sound():                                                                     # ne regarde pas le nom de la fonction sa marche quand même
    pygame.init()
    fenetre = pygame.display.set_mode((640,480))                                 # on creer la fenêtre et tout et tout le bazar
    fond = pygame.image.load("background.jpg").convert()
    fenetre.blit(fond, (0,0))
    perso = pygame.image.load("perso.png").convert_alpha()                       # le perso
    x=320
    y=240
    fenetre.blit(perso, (x,y))
    pygame.display.flip()
    clock = pygame.time.Clock()                                                  # c'est pour initialiser les FPS , tu le verras après


    continuer = 1                                                                #Variable de boucle



    pygame.key.set_repeat(1,20)                                                  # modifie les valeurs pour voir ce que ça fait
    while continuer:
        clock.tick(30)                                                           # 30 FPS , amuse-toi à les changé pour voir ; )
        for event in pygame.event.get():
            key=pygame.key.get_pressed()                                         # on regarde toutes les touches du clavier


            if event.type == QUIT:                                               # sa tu connais c'est pour sortir de la fenêtre
                continuer = 0
                pygame.quit()

            if  key[pygame.K_LEFT] :


                clock.tick(30)
                fenetre.blit(fond, (0,0))
                x = x-10

                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_RIGHT] :


                clock.tick(30)
                fenetre.blit(fond, (0,0))
                x = x+10

                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_UP] :


                clock.tick(30)
                fenetre.blit(fond, (0,0))
                y = y-10

                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_DOWN] :


                clock.tick(30)
                fenetre.blit(fond, (0,0))
                y = y+10

                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_DOWN] and key[pygame.K_LEFT]   :                    # A voila !!!! SI la touche (fleche bas et
                                                                                 # et fleche gauche sont appuyé alors:

                clock.tick(30)                                                   # FPS à 10 (tu peux modifier tout ça)
                fenetre.blit(fond, (0,0))
                y = y+10
                x=x-10
                fenetre.blit(perso, (x,y))
                pygame.display.flip()                                            # tu connais le reste on raffraichie l'écran et on blit le perso
                                                                                 # aux nouvelles coordonnées
            if  key[pygame.K_DOWN] and key[pygame.K_RIGHT] :


                clock.tick(30)
                fenetre.blit(fond, (0,0))
                y = y+10
                x= x+10

                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_UP] and key[pygame.K_RIGHT] :


                clock.tick(30)
                fenetre.blit(fond, (0,0))
                y = y-10
                x=x+10

                fenetre.blit(perso, (x,y))
                pygame.display.flip()

            if  key[pygame.K_UP] and key[pygame.K_LEFT] :


                clock.tick(30)
                fenetre.blit(fond, (0,0))
                y = y-10
                x=x-10

                fenetre.blit(perso, (x,y))
                pygame.display.flip()
sound()
