def rekt():
    from pos_boîte import position_boîte

    a=position_boîte()
    newliste=[]
    rekt_caisse=[]
    for x in range(0,len(a)):
        newliste=[]
        liste=[]
        recup = a[x]
        recup1=recup[0]
        recup2=recup[1]

        rekt_caisse.append([recup1,recup2,50,50])
    return(rekt_caisse)
