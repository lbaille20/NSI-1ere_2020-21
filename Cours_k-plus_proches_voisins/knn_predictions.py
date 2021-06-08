import matplotlib.pyplot as plt

def XYE_donnees_base(DonneesEtiquetees):
    nom0, nom1, nom2 = "iris setosa", "iris virginica", "iris versicolor"
    L0 = [ (float(e[0]), float(e[1])) for e in DonneesEtiquetees if e[2]=="0"]
    L1 = [ (float(e[0]), float(e[1])) for e in DonneesEtiquetees if e[2]=="1"]
    L2 = [ (float(e[0]), float(e[1])) for e in DonneesEtiquetees if e[2]=="2"]
    ##Liste des abscisses, liste des ordonnées pour "iris setosa"
    X0=[ longueur for longueur, largeur in L0]
    Y0=[ largeur for longueur, largeur in L0]
    ##Liste des abscisses, liste des ordonnées pour "iris virginica"
    X1=[ longueur for longueur, largeur in L1]
    Y1=[ largeur for longueur, largeur in L1]
    ##Liste des abscisses, liste des ordonnées pour "iris versicolor"
    X2=[ longueur for longueur, largeur in L2]
    Y2=[ largeur for longueur, largeur in L2]
    return X0, Y0, nom0, X1, Y1, nom1, X2, Y2, nom2

def graphique_donnees_base(listesXYE):
    X0, Y0, nom0, X1, Y1, nom1, X2, Y2, nom2 = listesXYE
    plt.title("Données de base de E. Anderson")
    plt.scatter(X0,Y0,color='red',label="iris setosa")
    plt.scatter(X1,Y1,color='blue',label="iris virginica")
    plt.scatter(X2,Y2,color='green',label="iris versicolor")
    plt.grid()
    plt.legend()
    plt.show()
    
##    
##iris_a = (3.5, 1.2)
##iris_b = (5.2, 1.3)
##iris_c = (2.1, 0,6)
##iris_d = (2.2, 1.0)
##iris_e = (4.0, 2.0)
##
##k=3
##prediction_espece_iris_a=0
##prediction_espece_iris_b=0
##prediction_espece_iris_c=0
##prediction_espece_iris_d=0
##prediction_espece_iris_e=0
##
####def couleur(i):
####    ...
####    return ...
##
##import matplotlib.pyplot as plt
##
##L0=[ (e[0], e[1]) for e in DonneesEtiquetees if e[2]=="0"]
##L1=[ (e[0], e[1]) for e in DonneesEtiquetees if e[2]=="1"]
##L2=[ (e[0], e[1]) for e in DonneesEtiquetees if e[2]=="2"]
##
##
##
##plt.scatter(X0,Y0,color='red',label="iris setosa")
##plt.scatter(X1,Y1,color='blue',label="iris virginica")
##plt.scatter(X2,Y2,color='green',label="iris versicolor")
##
####https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/marker_reference.html
####https://matplotlib.org/3.1.0/api/markers_api.html#module-matplotlib.markers
##
##""""
##https://stackoverflow.com/questions/14827650/pyplot-scatter-plot-marker-size
##
### doubling the width of markers
##x = [0,2,4,6,8,10]
##y = [0]*len(x)
##s = [20*4**n for n in range(len(x))]
##plt.scatter(x,y,s=s)
##plt.show()
##"""
##plt.scatter(3.5, 1.2, color='black', marker='s', s=30)
####plt.plot(X0,Y0,'ro',label="iris setosa")
####plt.plot(X1,Y1,'bo',label="iris virginica")
####plt.plot(X2,Y2,'go',label="iris versicolor")
##plt.grid()
##plt.xlabel("longueur des pétales")
##plt.ylabel("largeur des pétales")
##plt.legend()
####plt.savefig("iris base.png")
##plt.show()
##






