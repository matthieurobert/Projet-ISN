def répartition_obstacle():

    import random

    coordonnees=[]
    for x in range (100,1000,125):
        for y in range (100,600,125):
            coordonnees.append((x,y))

    random.shuffle(coordonnees)


    return (coordonnees)
