from obtenir import afficher_text
def save_score():
    import pickle
    from nom_score import nom
    from nom_score import nombre
    

    with open('score.txt','a') as score:

        score.write(nom())
        score.write(' ')
        score.write(nombre())
        score.write('\n')
    
    score.close()

save_score()
afficher_text()
