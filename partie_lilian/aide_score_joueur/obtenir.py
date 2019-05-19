def afficher_text():
    import pickle
    from nom_score import nom
    from nom_score import nombre


    with open('score.txt','r') as text_perso:
        info_perso = text_perso.read()
        score = info_perso.split()
        print(score[1])
   

