def nombre_caisse():
    from random import randrange # on créer une fonction qui donne un nombre
                                 # entre 5 et 14 ( c'est le nombre de caisses )
    nombre = randrange(5,15)

    return (nombre)

def nombre_caisse_spe(): # On verra ça plus tard si on rajoute

    from random import randrange    # des caisses spéciales

    nombre = randrange(1,4)

    return (int(nombre))