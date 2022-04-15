# Importation des modules
from random import uniform
import tkinter as tk


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

creer_fichier_alea(3, "Fichier_alea")

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

def moyenne(serie):
    """
    Fonction qui prend en paramètre une liste de réels représentants
    une qérie statistique.
    Fonction retourne la moyenne des réels.
    """
    somme = 0
    for elt in serie:
        somme += elt
    moyenne = somme / len(serie)
    return moyenne

def variance(serie):
    """
    Fonction qui prend en paramètre une liste de réels représentants
    une qérie statistique.
    Retourne la variance de la série
    """

# Constantes et Variables globale
width, height = 600, 600

# Création de la fenêtre
ecran = tk.Tk()

canvas = tk.Canvas(ecran, bg="black", width=width, height=height)
canvas.grid()
tk.Button(ecran, text="Graphique", command=lambda:print(trace_Nuage("Fichier_alea"))).grid()
#tk.Button(ecran, text="Trace_droite", command=lambda:(trace_droite(a, b)).grid()

# Création des axes du graphique
canvas.create_line(5, height-5, 5, 10, fill="blue")
canvas.create_line(5, height-5, width-10, height-5, fill="blue")

ecran.mainloop()