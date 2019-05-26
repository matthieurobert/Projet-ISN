
def lire_base_donner():

        import pickle
        from nom_score import nom
        from nom_score import nombre
        score_trier = []
        liste_classer = []
        liste_final = []
        score_pseudo = []
        liste_deuxiem =[]
        
        
        with open('score.txt','r') as text_perso:
                info_perso = text_perso.read()
                liste_depart = info_perso.split()
                
        for i in range (0,(len(liste_depart)),2) :
                        
                if i<((len(liste_depart))-1):
                        score_pseudo= [liste_depart[i],liste_depart[i+1]]
                score_trier.append(score_pseudo)
        liste_classer.append(score_trier[0])        
        for j in range (1,(len(score_trier)),1):
                dernier_liste_sclasser = int(len(liste_classer)-1)
                chiffre_comparais = int(score_trier[j][1])
                plus_grand_liste_classer = int(liste_classer[dernier_liste_sclasser][1])
                if (chiffre_comparais > plus_grand_liste_classer) :
                        liste_classer.append(score_trier[j])
                        position_liste = int(j)

        premier_score = liste_classer[(len(liste_classer)-1)]

        del score_trier(2):

        for n in range (1,(len(score_trier)),1):
                dernier_liste_sclasser2 = int(len(liste_classer)-1)
                chiffre_comparais2 = int(score_trier[n][1])
                deuxime_liste_classer = int(liste_classer[deuxime_liste_classer][1])
                if (chiffre_comparais2 > deuxime_liste_classer) :
                        liste_classer.append(score_trier[n])
                        position2_liste = n        

lire_base_donner()
