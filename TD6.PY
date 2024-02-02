def MoyenneMois(pays,temperature,moi ):
    som=0 
    for mois in pays :
        for i in mois:
            som=+i
             
        moy= som/len(mois)
    return moy