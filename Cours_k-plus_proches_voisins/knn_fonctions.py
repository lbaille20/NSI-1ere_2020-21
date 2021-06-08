from math import *
#distance entre deux données
def distance(a, b):
    """ a=(longueur iris 1, largeur iris 1) ;
        b=(longueur iris 2, largeur iris 2)"""
    somme = 0
    for i in range (len(a)):
        somme = somme + (a[i]-b[i])**2
    return sqrt(somme)

#Q7 : liste des distances d'une donnée nouvelle aux données de la base
def listeDistances(x,donnees_ref): 
    L=[]
    for i in range(len(donnees_ref)):
        L.append(distance(x,donnees_ref[i]))
    return L

#Q8 : indice de l'élément de l'ensemble de référence le plus proche de la donnée
def ppv(x,donnees_ref):
    """renvoie l'indice dans donnees_base de la donnée de base la
    plus proche de la nouvelle donnée x"""
    indice, dmin = -1, float('inf')
    for i in range(len(donnees_ref)):
        if distance(x,donnees_ref[i])<dmin:
            indice,dmin = i, distance(x,donnees_ref[i])
    return indice

##Séance 2
#Q3b
def k_ppv(x,donnees_ref,k):
    """renvoie la liste des indices des k plus proches voisins de la donnée x
    dans la liste des donnees de base donnees_base"""
    L=donnees_ref.copy()
    k_plus_proches=[]
    for i in range(k):
        i_ppv=ppv(x,L)
        k_plus_proches.append(i_ppv)
        L[i_ppv]=[float('inf'), float('inf')]
    return k_plus_proches

#Q4b
##def k_ppv2(x,L,k):
##    #construction de la liste des distances
##    D=listeDistances(x,L)
##    #détermination des k plus petites distances
##    distances_triées=sorted(D)
##    k_plus_petites_distances=distances_triées[:k]
##    print(k_plus_petites_distances)
##    #recherche des indices dans D des k plus petites distances
##    indices=[]
##    i=0
##    while i<len(D) and len(indices)<k:
##        if D[i] in k_plus_petites_distances:
##            indices.append(i+1)
##        i+=1
##    return indices

def determine_etiquettes(Etiquettes, Indices):
    """renvoie les étiquettes pour tous les éléments
    dont les indices de position dans la liste Donnees
    sont dans la liste Indices"""
    return [ Etiquettes[i][-1] for i in Indices]

def decompte(E):
    """renvoie un triplet (nbZeros, nbUn, nbDeux) dont les éléments sont
    les nombres d'éléments de la liste d'étiquettes E, qui portent, respectivement,
    l'étiquette '0', l'étiquette '1', l'étiquette '2'"""
    nbZeros, nbUn, nbDeux = 0, 0, 0
    for e in E:
        if e=='0':
            nbZeros+=1
        elif e=='1':
            nbUn+=1
        else:
            nbDeux+=1
    return nbZeros, nbUn, nbDeux

def i_maximum3(effectifs):
    """renvoie l'indice de l'effectif maximal
    pour une liste 3 effectifs"""
    a,b,c=effectifs
    if a < b:
        i_max=1
    else:
        i_max=0
    if effectifs[i_max]>c:
        return i_max
    else:
        return 2

def i_maximum(effectifs):
    """renvoie l'indice de l'effectif maximal
    pour une liste quelconque d'effectifs"""
    i_max, eff_max = 0, effectifs[0]
    for j in range(1,len(effectifs)):
        if effectifs[j]>eff_max:
            i_max = j
    return str(i_max)

##Chaînage des fonctions
def predire(Etiquettes, Indices):
    """renvoie à partir de la liste des étiquettes des données
    et d'un sous-ensemble d'indices parmi les données
    l'étiquette majoritaire dans ce sous-ensemble de données"""
    etiquettes=determine_etiquettes(Etiquettes, Indices)
    effectifs=decompte(etiquettes)
    return i_maximum(effectifs)
