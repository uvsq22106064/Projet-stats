# Importation des modules
from operator import truediv
from random import uniform
import tkinter as tk
from math import sqrt

def creer_fichier_alea(nb, nomfichier):
    """
    Fonction qui prend un nb en entier et un nomfichier en string.
    Fonction quiva créer un fichier texte avec commme nom
    l'argument nomfichier, avec nbr de lignes correspondant a
    l'argument nb.
    Chaque ligne contiendra deux nbrs aleatoires flottants
    """
    file = open(nomfichier, "w", encoding="Utf-8")
    i = 0
    while i != nb:
        file.write(f"{uniform(0, 500)} {uniform(0, 500)}\n")
        i += 1

    file.close()

creer_fichier_alea(45, "Fichier_alea")

def lit_fichier(nomfic):
    """
    Fonction qui prend en argument un nom de fichier en string.
    Fichier qui contient deux coordonées par lignes séparés d'un espace
    Fonction va lire le fichier et renvoyer la liste des X et liste Y
    """
    file = open(nomfic, "r")
    listeX, listeY, = [], []

    for ligne in file:
        a = ligne.split()
        listeX.append(a[0])
        listeY.append(a[1])

    file.close()
    return listeX, listeY

#print(lit_fichier("Fichier_alea"))

def trace_Nuage(nomf):
    """
    Fonction qui prend en argument le nom d'un fichier en string.
    Fichier qui contient les coordonées des points d'un nuage.
    Fonction va appeler la fonction lit_fichier puis va représenter
    le nuage de points correspondant.Puis renverra le nombre de points
    dessinés.
    """
    global height
    liste_points = lit_fichier(nomf)
    for i in range(len(liste_points[0])):
        canvas.create_oval(float(liste_points[0][i]) + 5,     height - float(liste_points[1][i]),
                           float(liste_points[0][i]) + 7, (height - float(liste_points[1][i])) + 2,
                           fill="red")

    nbr_points = len(liste_points[0])   # ou de liste_points[1]
    return nbr_points


def trace_droite(a, b):
    """
    Fonction qui prend duex flottants en arguments
    a = coefficient directeur et b =l'ordonée à l'origine.
    Tracer une droitye entre l'ordonée à l'origine et
    le coefficient directeur
    """
    global height, width
    fonction_lineaire = a * width + b
    x0 = 0
    y0 = height - b
    x1 = width       # longueur max de la droite
    y1 = height - fonction_lineaire
    canvas.create_line(x0, y0, x1, y1, fill="green")





def moyenne(serie):
    somme = 0
    for elt in serie:
        somme += elt
    moyenne = somme / len(serie)
    return serie

def variance(serie):
    moyenne_serie = moyenne(serie)
    somme = 0
    for elt in serie:
        somme += (elt - moyenne_serie)**2
    variance_serie = somme / len(serie)
    return variance_serie

def covariance(serieX, serieY):
    moyenne_serieX = moyenne(serieX) 
    moyenne_serieY = moyenne(serieY)
    produit = 0
    for i in range(len(serieX)):
        produit += (serieX[i] - moyenne_serieX)*((serieY[i] - moyenne_serieY))
    covariance_series = produit / len(serieX)
    return covariance_series

def correlation(serieX, serieY):
    coefficient_correlation_lineaire = 0
    variance_serieX = variance(serieX) 
    variance_serieY = variance(serieY)
    covariance_series = covariance(serieX, serieY)
    correlation_series = covariance_series // (sqrt(variance_serieX * variance_serieY))
    return correlation_series

def forteCorrelation(serieX, serieY):
    
    corr = correlation(serieX, serieY)

    if 1 > corr > 0.8 or -1 < corr < -0.8:
        return True
    else :
        return False 

def droite_reg(serieX, serieY):
    a = covariance(serieX,serieY)/variance(serieX)
    b= moyenne(serieY) - a * moyenne(serieX)
    return (a,b)


# Constantes et Variables globale
width , height = 600, 600
heights = 595

# Création de la fenêtre
ecran = tk.Tk()

canvas = tk.Canvas(ecran, bg="black", width=width, height=height)
canvas.grid()
tk.Button(ecran, text="Graphique", command=lambda:print(trace_Nuage("Fichier_alea"))).grid()
tk.Button(ecran, text="Trace_droite", command=lambda:(trace_droite(5, 4))).grid()
tk.Button(ecran, text="Trace_droite", command=lambda:(trace_droite(5, 4))).grid()



# Création des axes du graphique
canvas.create_line(5, heights, 5, 10, fill="blue")
canvas.create_line(5, heights, width-10, heights, fill="blue")

ecran.mainloop()