def save_score():
    import pickle
    from nom_score import nom
    from nom_score import nombre


    with open('score.txt','r') as score:

        score.write(nom())
        score.write(' ')
        score.write(nombre())
        score.write('\n')

    enregister = pickle.Pickler(score)

save_score()