def position_boîte():
    from coordonnées_aléatoire import répartition_obstacle
    from nombre_obstacle import nombre_caisse
    from random import randrange

    nombres = nombre_caisse()


    coordonnee = répartition_obstacle()
    modif_coordonnee = []


    for x in range (0,nombres,1):


        randx = randrange(-50,51)
        randy = randrange(-50,51)

        recuperateur = []
        recuperateur = coordonnee[x]
        recup1 = recuperateur[0]
        recup2 = recuperateur[1]


        modif_coordonnee.append((recup1+randx,recup2+randy))

    return(modif_coordonnee)




