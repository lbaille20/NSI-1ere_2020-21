#Chargement des données
##https://docs.python.org/fr/3.6/library/csv.html
def chargementDonnees(nomFichier):
    import csv
    with open (nomFichier, 'r') as f:
        lignes = csv.reader(f)
        tableau = list(lignes)
    return tableau

##def traitementDonnees(T):
##    D=[]
##    for k in range(len(T)):
##        D=[float(T[k][i] for i in range(len(T[k])-1)]+[T[k][-1]]
##    return D
           
DonneesEtiquetees=chargementDonnees("iris.csv")
##DonneesEtiquetees=traitementDonnees(chargementDonnees("iris.csv"))

#Scinder en donnees et étiquettes
def extraction_donnees_etiquettes(T):
    donnees, etiquettes = [], []
    for k in range(1,len(T)): #départ à 1 pour supprimer les en-têtes
        longueur, largeur, espèce = T[k]
        donnees.append([float(longueur),float(largeur)])
        etiquettes.append(espèce)
    return donnees, etiquettes

Donnees, Etiquettes = extraction_donnees_etiquettes(DonneesEtiquetees)

##PARTITION DES DONNEES
def partionnementDonneesEtiquetees(D, E, etiquettes=["0","1","2"]):
    """renvoie, à partir de la liste des données
    et de la liste des étiquettes
    les listes des valeurs des attributs pour chaque étiquette"""
    donnees_partitionnees=[[] for e in etiquettes]
    for k in range(len(D)):
        d, e = D[k], E[k] #d : k_ème donnée, e : étiquette de la k_ème donnée
        #on ajoute la donnée à la liste de données pour cette étiquette
        donnees_partitionnees[etiquettes.index(e)].append(d)
    #on renvoie la liste des couples (étiquettes, données portant cette étiquette)
    return [(etiquettes[k], donnees_partitionnees[k]) for k in range(len(etiquettes))]

#partitionnement des données
DE0, DE1, DE2 = partionnementDonneesEtiquetees(Donnees, Etiquettes)
##Abscisses et ordonnées pour les données d'étiquette "0"
X0 = [d[0] for d in DE0[1]]
Y0 = [d[1] for d in DE0[1]]
##Abscisses et ordonnées pour les données d'étiquette "1"
X1 = [d[0] for d in DE1[1]]
Y1 = [d[1] for d in DE1[1]]
##Abscisses et ordonnées pour les données d'étiquette "2"
X2 = [d[0] for d in DE2[1]]
Y2 = [d[1] for d in DE2[1]]

#couleurs pour les différentes espèces
c0="green" ## iris setosa
c1="red"   ## iris virginica
c2="blue"  ## iris versicolor
