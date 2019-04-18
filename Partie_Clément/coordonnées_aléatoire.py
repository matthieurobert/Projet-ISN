def répartition_obstacle():    # création de la fonction répartition_obstacle

    import random              # on importe random

    coordonnees=[]             # initialisation de la liste coordonnées
    for x in range (100,1000,125):
        for y in range (100,600,125):
            coordonnees.append((x,y)) # on ajoute à la liste des coordonnées

    random.shuffle(coordonnees) # on mélange la liste


    return (coordonnees)  # on renvoie la valeur coordonnées
