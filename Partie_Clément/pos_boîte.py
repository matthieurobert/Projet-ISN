def position_boîte():
    from  Partie_Clément.coordonnées_aléatoire import répartition_obstacle       # on importe les fonction nommbre caisse et
    from  Partie_Clément.nombre_obstacle import nombre_caisse                    # répartition obstacle
    from random import randrange

    nombres = nombre_caisse()


    coordonnee = répartition_obstacle()
    modif_coordonnee = []


    for x in range (0,nombres,1):


        randx = randrange(-25,25)                                                # on créer des coordonnées aléatoires de -25 à +25 d'écart
        randy = randrange(-25,25)                                                # par rapport à ceux d'origines

        recuperateur = []
        recuperateur = coordonnee[x]
        recup1 = recuperateur[0]
        recup2 = recuperateur[1]


        modif_coordonnee.append((recup1+randx,recup2+randy))                     # on rajoute la valeur  en x et y de chaques coordonnées

    return(modif_coordonnee) # renvoie modif_coordonnée




