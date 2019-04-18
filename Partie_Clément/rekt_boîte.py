import pygame

def rekt():

    from  Partie_Clément.salle import salle # on importe la liste de la
                                            #  fonction salle
    a=salle()
    c=list(a)

    b=a[4] # on récupère la 4ème  valeur (  position_x_y  )

    newliste=[]
    rekt_caisse=[]
    for x in range(0,len(b)):
        newliste=[]
        liste=[]
        recup = b[x]
        recup1=recup[0]      # On récupère chaque valeur de chaques coordonnées
        recup2=recup[1]           # on ajoute le rect de la boîte qui est 50,50
        rect = pygame.Rect(recup1,recup2,50,50)
        rekt_caisse.append(rect)
    rekt_caisse.append(c)               # on remet le reste dans le rekt_caisse
                                         # soit la fonction salle


    return(rekt_caisse) # on renvoie le rect
