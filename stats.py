# Importation des modules
from random import uniform , randint
import tkinter as tk
from math import sqrt
import os as os
from tkinter.filedialog import askopenfilename
# Création des fonctions

# PARTIE 1

def creer_fichier_alea(nb, nomfichier):
    """
    Fonction qui prend un nb en entier et un nomfichier en string.
    Fonction qui va créer un fichier texte avec commme nom
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
        listeX.append(float(a[0]))
        listeY.append(float(a[1]))

    file.close()
    return listeX, listeY





def trace_Nuage(nomf):
    """
    Fonction qui prend en argument le nom d'un fichier en string.
    Fichier qui contient les coordonées des points d'un nuage.
    Fonction va appeler la fonction lit_fichier puis va représenter
    le nuage de points correspondant.Puis renverra le nombre de points
    dessinés.
    """
    global height, l_y, l_x
    # Création des axes du graphique
    canvas.create_line(5, heights, 5, 10, fill="blue")
    canvas.create_line(5, heights, width-10, heights, fill="blue")
    liste_points = lit_fichier(nomf)
    for i in range(len(liste_points[0])):
        canvas.create_oval(float(liste_points[0][i]) + 5,  height - float(liste_points[1][i]),
                           float(liste_points[0][i]) + 9, (height - float(liste_points[1][i])) + 4,
                           fill="red")

    nbr_points = len(liste_points[0])   # ou de liste_points[1]

    # récupère les deux listes de coordonées
    l_x = liste_points[0].copy()
    l_y = liste_points[1].copy()
    

    return nbr_points





def trace_droite(a, b):
    """
    Fonction qui prend duex flottants en arguments
    a = coefficient directeur et b =l'ordonée à l'origine.
    Tracer une droitye entre l'ordonée à l'origine et
    le coefficient directeur
    """
    global height, width, couleur, liste, peut_tracer, l_x, l_y
    #calcule de la correlation
    if len(l_x) != 0:
        peut_tracer = forteCorrelation(l_x, l_y)
    if peut_tracer == True:
        fonction_lineaire = a * width + b
        x0 = 5
        y0 = height - b
        x1 = width       # longueur max de la droite
        y1 = height - fonction_lineaire
        ligne = canvas.create_line(x0, y0, x1, y1, fill= couleur, width=2)
        liste.append(ligne)


# Série de test partie 1
#creer_fichier_alea(50, "Fichier_alea")
#print(lit_fichier("Fichier_alea"))
# Les 2 tests si dessous s'éxécutent vers la fin du programme
#tk.Button(ecran, text="Graphique", command=lambda:print(trace_Nuage("Fichier_alea"))).grid()
#tk.Button(ecran, text="Trace_droite", command=lambda:(trace_droite(5, 4))).grid()


# PARTIE 2

def moyenne(serie):
    """Fonction qui renvoi la moyenne d'une série"""
    somme = 0
    for elt in serie:
        somme += elt
    moyenne = somme / len(serie)
    return moyenne





def variance(serie):
    """Fonction qui renvoi la variance d'une série"""
    moyenne_serie = moyenne(serie)
    somme = 0
    for elt in serie:
        somme += (elt - moyenne_serie)**2
    variance_serie = somme / len(serie)
    return variance_serie





def covariance(serieX, serieY):
    """Fonction qui renvoi la covariance entre deux séries"""
    moyenne_serieX = moyenne(serieX) 
    moyenne_serieY = moyenne(serieY)
    produit = 0
    for i in range(len(serieX)):
        produit += (serieX[i] - moyenne_serieX)*((serieY[i] - moyenne_serieY))
    covariance_series = produit / len(serieX)
    return covariance_series





def correlation(serieX, serieY):
    """Fonction qui renvoi la correlation entre deux séries"""
    coefficient_correlation_lineaire = 0
    variance_serieX = variance(serieX) 
    variance_serieY = variance(serieY)
    covariance_series = covariance(serieX, serieY)
    correlation_series = covariance_series / (sqrt(variance_serieX * variance_serieY)) 
    return correlation_series





def forteCorrelation(serieX, serieY):
    """Fonction qui prend deux listes de nombres flottants en argument
    et verifie si il y a une forte correlation entre les deux listes
    elle renvoie donc un booléen"""
    corr = correlation(serieX, serieY)
    if -0.8 < corr < 0.8:
        return False
    else :
        return True





def droite_reg(serieX, serieY):
    """Fonction qui Trace a partir des les listes de Position x et y, la droite de regression"""
    a = covariance(serieX,serieY)/variance(serieX) # coefficient directeur
    b= moyenne(serieY) - a * moyenne(serieX) # ordonée à l'origine
    return (a,b)





def aide():
    """Fonction qui renvoi vers le README de Github"""
    os.system("start https://github.com/uvsq22106064/Projet-stats#readme")





def charger():
    """Charge une configuration choisit par l'utilisateur."""
    global filename
    filename = askopenfilename(title="Charger une configuration", filetypes=[
                               ("Fichier .txt", ".txt")])


# Série de test partie 2
#print(moyenne([4, 6, 5, 6, 8, 4, 6, 5, 10, 5]))
#print(moyenne([7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(variance([7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(covariance([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(correlation([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(forteCorrelation([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(droite_reg([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))


# PARTIE 3

def changer_couleur():
    global couleur, liste_couleur, couleur, liste
    couleur = liste_couleur[randint(0, len(liste_couleur)-1)]
    
# Programme Principale

# Constantes et Variables globale
width , height = 600, 600
heights = 595
liste = []
liste_couleur = ["green", "blue", "red", "yellow", "orange", "purple", 
"white", "pink"]
couleur = liste_couleur[randint(0, len(liste_couleur)-1)]
peut_tracer = True
l_x, l_y = [], []


# Création de la fenêtre
ecran = tk.Tk()

canvas = tk.Canvas(ecran, bg="black", width=width, height=height)
canvas.grid(row=0 ,column=0, columnspan=3)
tk.Button(ecran, text="Graphique", command=lambda:print(trace_Nuage("Fichier_alea"))).grid(row=1 ,column=0)
tk.Button(ecran, text="Trace_droite", command=lambda:(trace_droite(randint(0,3),randint(0,100)))).grid(row=1 ,column=1)
tk.Button(ecran, text="Quitter", command=ecran.quit).grid(row=1 ,column=2)
tk.Button(ecran, text="Autre couleur", command=changer_couleur).grid(row=2 ,column=2)


#Créer une fenêtre graphqiue comportant un canevas et trois boutons
#pour lancer les différentes fonctions
#Screen= tk.Toplevel()
#tk.Button(text="Tracer la droite", command=lambda: trace_droite(droite_reg(lit_fichier("Fichier_alea")[0], lit_fichier("Fichier_alea")[1]))).grid()
##tk.button(text="Autre couleur", command=lambda: ).grid()
#tk.Button(text="Quitter", command=closing_window).grid()


# Création des axes du graphique
canvas.create_line(5, heights, 5, 10, fill="blue")
canvas.create_line(5, heights, width-10, heights, fill="blue")
ecran.mainloop()
#Screen.mainloop()
