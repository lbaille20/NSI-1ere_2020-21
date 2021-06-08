##PARTITION DES DONNEES
def partionnementDonneesEtiquetees(D, E, etiquettes=["0","1","2"]):
    """renvoie, à partir de la liste des données
    et de la liste des étiquettes
    les listes des valeurs des attributs pour chaque étiquette"""
    donnees_partitionnées=[[] for e in etiquettes]
    for k in range(len(D)):
        d, e = D[k], E[k] #d : k_ème donnée, e : étiquette de la k_ème donnée
##        print(d,e)
##        print(donnees_partitionnées)
##        print(etiquettes.index(e))
##        input("continuer ?")
        #on ajoute la donnée à la liste de données pour cette étiquette
        donnees_partitionnées[etiquettes.index(e)].append(d)
##        print(donnees_partitionnées)
##        input("continuer ?")
    #on renvoie la liste des couples (étiquettes, données portant cette étiquette)
    return [(etiquettes[k], donnees_partitionnées[k]) for k in range(len(etiquettes))]
   
