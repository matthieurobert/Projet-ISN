import random
def liste():
    liste_bot = [(1040,640,50,50),(1040,460,50,50),(1040,340,50,50),(1040,160,50,50),(0,340,50,50),(0,400,50,50),(0,580,50,50),(0,220,50,50),(0,150,50,50),(0,50,50,50),(0,110,50,50),(0,180,50,50),(0,240,50,50),(0,290,50,50),(1040,590,50,50),(1040,520,50,50),(1040,280,50,50),(1040,400,50,50),(1040,210,50,50)]
    random.shuffle(liste_bot)
    return(liste_bot)

# Explication :
# On a un liste_bot contenant une liste de coordonnées
# on mélange
# On renvoie la liste_bot
