import matplotlib.pyplot as plt
from knn_fonctions import *

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

##
##https://stackoverflow.com/questions/24943991/change-grid-interval-and-specify-tick-labels-in-matplotlib
##ref. : https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.axes.Axes.grid.html
g = 2.5
l, h = 7*g, 2.5*g*2
fig_size=(l, h)
##plt.rcParams["figure.figsize"] = fig_size
X0, Y0, nom0, X1, Y1, nom1, X2, Y2, nom2 = XYE_donnees_base(DonneesEtiquetees)

###
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
plt.ion()
fig, ax = plt.subplots(figsize=fig_size)
plt.title("Classification des cinq iris exemples", fontsize=24)
plt.scatter(X0,Y0,color='red',label="iris setosa")
plt.scatter(X1,Y1,color='blue',label="iris virginica")
plt.scatter(X2,Y2,color='green',label="iris versicolor")

# Set axis ranges; by default this will put major ticks every <...>.
plt.xlim(0, 7.5)
plt.ylim(0, 3.0)

# Change major ticks to show every 20.
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(0.5))

# Change minor ticks to show every 0.1 ()
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

# Turn grid on for both major and minor ticks and style minor slightly
# differently.
ax.grid(which='major', color='#CCCCCC', linestyle='--')
ax.grid(which='minor', color='#CCCCCC', linestyle=':')
plt.xlabel('longueur des pétales', fontsize=18)
plt.ylabel('largeur des pétales', fontsize=18)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
plt.legend(loc='upper left', fontsize=16)
"""
Traitement des iris
"""
iris_a = ('a', 3.5, 1.2)#1.2
iris_b = ('b', 5.2, 1.3)
iris_c = ('c', 2.5, 0.6)#2.5
iris_d = ('d', 2.2, 1.0)
iris_e = ('e', 4.0, 2.0)
t=(iris_a, iris_b, iris_c, iris_d, iris_e)
for iris in t:
    denom, x, y = iris
    plt.scatter(x,y,color="orange",marker="^")
    plt.annotate(denom,
         xy=(x, y), xycoords='data',
         xytext=(+15, +20), textcoords='offset points',\
             fontsize=12,
         arrowprops=dict(arrowstyle="->", \
                         connectionstyle="arc3,rad=.2"))
##http://www.learningaboutelectronics.com/Articles/How-to-draw-a-circle-using-matplotlib-in-Python.php
##https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.patches.Circle.html
    c=plt.Circle((x,y), radius= distance((x,y),Donnees[k_ppv((x,y),Donnees,3)[-1]]), edgecolor="orange", fill=False)
    ax.add_patch(c)
plt.axis('equal')
"""
Fin traitement des iris
"""
plt.savefig("fig01 - Classification des 5 exemples.png")

plt.show()





