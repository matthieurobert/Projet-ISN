def position_boîte():
    from  Partie_Clément.coordonnées_aléatoire import répartition_obstacle
    from  Partie_Clément.nombre_obstacle import nombre_caisse
    from random import randrange

    nombres = nombre_caisse()


    coordonnee = répartition_obstacle()
    modif_coordonnee = []


    for x in range (0,nombres,1):


        randx = randrange(-25,25)
        randy = randrange(-25,25)

        recuperateur = []
        recuperateur = coordonnee[x]
        recup1 = recuperateur[0]
        recup2 = recuperateur[1]


        modif_coordonnee.append((recup1+randx,recup2+randy))

    return(modif_coordonnee)




