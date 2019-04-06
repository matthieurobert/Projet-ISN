import pygame

def rekt():

    from  Partie_Clément.salle import salle

    a=salle()
    c=list(a)
    del a[0]
    del a[0]
    del a[0]
    del a[0]

    for x in range(0,1):
        b=a[0]



    newliste=[]
    rekt_caisse=[]
    for x in range(0,len(b)):
        newliste=[]
        liste=[]
        recup = b[x]
        recup1=recup[0]
        recup2=recup[1]
        rect = pygame.Rect(recup1,recup2,50,50)
        rekt_caisse.append(rect)
    rekt_caisse.append(c)


    return(rekt_caisse)
