import random
def liste():
    liste_bot = [(1076,640,50,50),(1076,460,50,50),(1076,340,50,50),(1076,160,50,50),(6,340,50,50),(6,400,50,50),(6,580,50,50),(6,220,50,50),(6,150,50,50),(6,50,50,50),(6,110,50,50),(6,180,50,50),(6,240,50,50),(6,290,50,50),(1076,590,50,50),(1076,520,50,50),(1076,280,50,50),(1076,400,50,50),(1076,210,50,50)]
    random.shuffle(liste_bot)
    return(liste_bot)

# Explication :
# On a un liste_bot contenant une liste de coordonnées
# on mélange
# On renvoie la liste_bot
