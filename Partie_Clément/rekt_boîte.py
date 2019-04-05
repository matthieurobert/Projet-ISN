import pygame

def rekt():

    from  Partie_Clément.pos_boîte import position_boîte

    a=position_boîte()
    newliste=[]
    rekt_caisse=[]
    for x in range(0,len(a)):
        newliste=[]
        liste=[]
        recup = a[x]
        recup1=recup[0]
        recup2=recup[1]
        rect = pygame.Rect(recup1,recup2,50,50)
        rekt_caisse.append(rect)

    return(rekt_caisse)

