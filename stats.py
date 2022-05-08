# Importation des modules
from random import uniform , randint
import tkinter as tk
import os as os
import pandas
from tkinter.filedialog import askopenfilename

from pyrsistent import v

# Création des fonctions
# PARTIE 1

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


def lit_fichier(nomfic):
    """
    Fonction qui prend en argument un nom de fichier en string.
    Fichier qui contient deux coordonées par lignes séparés d'un espace
    Fonction va lire le fichier et renvoyer la liste des X et liste Y
    """
    if nomfic == "Fichier_alea":
        creer_fichier_alea(50, "Fichier_alea")
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
    global height, liste_y, liste_x, liste_tracer_droite, width
    canvas.delete("all")
    # Création des axes du graphique
    tracer_axes()
    liste_points = lit_fichier(nomf)
    for i in range(len(liste_points[0])):
        canvas.create_oval(float(liste_points[0][i]) + 15,   height - float(liste_points[1][i]) - 15,
                           float(liste_points[0][i]) + 19,   height - float(liste_points[1][i]) - 19,
                           fill="red")

    nbr_points = len(liste_points[0])   # ou de liste_points[1]
    # récupère les deux listes de coordonées
    liste_x = liste_points[0].copy()
    liste_y = liste_points[1].copy()
    
    j = droite_regression(liste_x,liste_y)
    liste_tracer_droite.insert(0, j[1])
    liste_tracer_droite.insert(0, j[0])
    return nbr_points


def trace_droite(a, b):
    """
    Fonction qui prend duex flottants en arguments
    a = coefficient directeur et b =l'ordonée à l'origine.
    Tracer une droitye entre l'ordonée à l'origine et
    le coefficient directeur
    """
    global height, width, couleur, liste, peut_tracer, liste_x, liste_y
    #calcule de la correlation
    if len(liste_x) != 0:
        peut_tracer = forteCorrelation(liste_x, liste_y)
    
    if peut_tracer == True:
        fonction_lineaire = a * 635 + b
        x0 = 15
        y0 = height - 15 - b
        x1 = width       # longueur max de la droite
        y1 = height - 15 - fonction_lineaire 
        ligne = canvas.create_line(x0, y0, x1, y1, fill= couleur, width=2)
        liste.append(ligne)

def tracer_axes():
    """
    Fonction qui va tracer les axes x et y 
    """
    canvas.create_line(15, 635, 15, 50, fill="blue")
    canvas.create_line(15, 635, 600, 635, fill="blue")
    # tracer les deux flèches au bout des deux axes
    canvas.create_line(596, 631,600, 635)
    canvas.create_line(596, 639,600, 635)
    canvas.create_line(11, 54, 15, 50)
    canvas.create_line(19, 54, 15, 50)
    # Tracer les graduations des deux axes. 
    # Echelles 1 barres = 50
    val = 50
    canvas.create_text(10, 645, text=0)
    for i in range(65, 575, 50):
        canvas.create_line(i, 632, i, 638, fill="blue")
        canvas.create_line(12,  650-i, 18, 650-i, fill="blue")
        canvas.create_text(28, 645-i, text=val)
        canvas.create_text(i, 645, text=val)
        val += 50


# PARTIE 2

def moyenne(serie):
    """Fonction qui renvoi la moyenne d'une série"""
    somme = 0
    for elt in serie:
        somme += float(elt)   
    moyenne = somme / len(serie)
    return moyenne



def variance(serie):
    """Fonction qui renvoi la variance d'une série"""
    moyenne_serie = moyenne(serie)
    somme = 0
    for elt in serie:
        somme += (float(elt) - moyenne_serie)**2
    variance_serie = somme / len(serie)
    return variance_serie


def covariance(serieX, serieY):
    """Fonction qui renvoie la covariance entre deux séries"""
    moyenne_serieX = moyenne(serieX) 
    moyenne_serieY = moyenne(serieY)
    produit = 0
    for i in range(len(serieX)):
        produit += (float(serieX[i]) - moyenne_serieX)*((float(serieY[i]) - moyenne_serieY))
    covariance_series = produit / len(serieX)
    return covariance_series


def correlation(serieX, serieY):
    """Fonction qui renvoi la correlation entre deux séries"""
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
    corr = round(corr)
    if (-1 <= corr <= -0.8) or  (0.8 <= corr <= 1):
        return True
    else :
        return False
 
def droite_regression(serieX, serieY):
    """Fonction qui Trace a partir des les listes de Position x et y, la droite de regression"""
    a = covariance(serieX,serieY) / variance(serieX)
    b = moyenne(serieY) - a * moyenne(serieX)
    return (a,b)


def aide():
    """Fonction qui renvoi vers le README de Github"""
    os.system("start https://github.com/uvsq22106064/Projet-stats#readme")
    

# PARTIE 3

def changer_couleur():
    """ Va tirer une couleur aléatoire pour la changer au prochain tracé"""
    global couleur, liste_couleur
    couleur = liste_couleur[randint(0, len(liste_couleur)-1)]

def desactiver():
    """
    Va retirer la fonctionalité d'ajouter des points manuellements.
    """
    global dessin
    dessin = False

def activer():
    """ 
    Va activer la fonctionalité d'ajouter des points manuellements.
    """
    global dessin
    dessin = True

def ajout_point(event):
    """ 
    Ajoute des points dès que l'on clique.
    """
    global liste_x, liste_y, dessin, liste
    if dessin == True:
        canvas.create_oval(event.x ,  event.y,
                           event.x + 4,  event.y + 4,
                           fill="red")
        liste_x.append(event.x)
        liste_y.append(event.y)
        if len(liste_x) > 2:                        # peut pas tracer de droites tant que l'on a pas plus de deux points
            if len(liste) != 0:                     # supprime la ligne précédante 
                canvas.delete(liste[-1])
            j = droite_regression(liste_x,liste_y)
            liste_tracer_droite.insert(0, j[1])
            liste_tracer_droite.insert(0, j[0])       

        
def extraire_info_fichier():
    """ Extrait les infos du fichier villes_virgules.csv en utlisant la bibliothèque pandas
    puis trace le nombre d habitants de 2010 en fonction du nombre d'habitants de 2012."""
    global liste_x, liste_y, nombre_choisi, height
    liste_x, liste_y = [], []
    canvas.delete("all")
    tracer_axes()
    if nombre_choisi != 0:
        info_villes = pandas.read_csv("villes_virgule.csv")
        a = info_villes.loc[(info_villes["nb_hab_2010"] <= 500) & (info_villes["nb_hab_2012"] <= 500) , ["nb_hab_2010", "nb_hab_2012"]]
        # tolist() va permettre de récupérer les valeurs de la colone choisis dans la base qu'on a récupérer à la ligne précedante
        nb_2010 = a["nb_hab_2010"].tolist()             
        nb_2012 = a["nb_hab_2012"].tolist()
        
        file = open("donnees_villes_hab", "w")
        for i in range(nombre_choisi):
            file.write(f"{int(nb_2010[i])} {int(nb_2012[i])}\n")
        file.close()
        file_2 = open("donnees_villes_hab", "r")
        for i in range(nombre_choisi):
            ligne = file_2.readline()
            coords = ligne.split()
            liste_x.append(coords[0])
            liste_y.append(coords[1])
        file_2.close()
        for i in range(nombre_choisi):
            canvas.create_oval(float(liste_x[i]) + 15,  height - (float(liste_y[i]) - 15),
                               float(liste_x[i]) + 19,  height - (float(liste_y[i]) - 19),
                               fill="red")

        j = droite_regression(liste_x,liste_y)
        liste_tracer_droite.insert(0, j[1])
        liste_tracer_droite.insert(0, j[0])    



def extraire_info_fichier_2():
    """
    Extrait les infos du fichier anscombes.csv en utlisant la bibliothèque pandas
    puis trace les cooordonnées de la colone Y1 en fonction des coordonées de la colone X1.
    """
    global liste_x, liste_y, nombre_choisi
    liste_x, liste_y = [], []
    canvas.delete("all")
    tracer_axes()
    if nombre_choisi != 0:
        coords = pandas.read_csv("anscombe.csv")
        liste = coords.columns.tolist()
        a = coords.loc[: , [liste[2], liste[1]]]    # colones "X", "Y1"
        # tolist() va permettre de récupérer les valeurs de la colone choisis dans la base qu'on a récupérer à la ligne précedante
        points_Y1 = a[liste[2]].tolist()             
        points_X =  a[liste[1]].tolist()
        file = open("ansconbes.txt", "w")
        for i in range(nombre_choisi):
            file.write(f"{int(points_X[i])} {int(points_Y1[i])}\n")
        file.close()
        file_2 = open("ansconbes.txt", "r")
        for i in range(nombre_choisi):
            ligne = file_2.readline()
            p = ligne.split()
            liste_x.append(p[0])
            liste_y.append(p[1])
            
        file_2.close()
       
        for i in range(nombre_choisi):
            print(int(liste_y[i]))
            canvas.create_oval(float(liste_x[i]) + 15,  height - (float(liste_y[i])) - 15,
                               float(liste_x[i]) + 19,  height - (float(liste_y[i])) - 19,
                               fill="green")

        j = droite_regression(liste_x,liste_y)
        liste_tracer_droite.insert(0, j[1])
        liste_tracer_droite.insert(0, j[0])    

def valeur_entrer():
    """
    Récupère la valeur entrer par l'utilisateur après avoir appuyer sur le 
    bouton valider. 
    """
    global nombre_choisi
    nombre_choisi = int(entry.get())
    

# Bonus

def sauvegarde_configuration():
    """
    Sauvegarder une configuration en cours
    """
    global liste_x, liste_y
    file = open("sauvegarde_configuration", "w")
    for i in range(len(liste_x)):
        file.write(f"{liste_x[i]} {liste_y[i]}\n")
        
    file.close()

def recuperer_configuration():
    """
    Lit le fichier ou l'on as sauvegardé une configuration puis on l'affiche.
    """
    global liste_x, liste_y, liste_tracer_droite
    liste_x, liste_y = [], []
    file = open("sauvegarde_configuration", "r")
    while 1:
        ligne = file.readline()
        a = ligne.split()
        if ligne == "":
            break
        liste_x.append(a[0])
        liste_y.append(a[1])
    file.close()
    tracer_axes()
    
    for i in range(len(liste_y)):
        canvas.create_oval(float(liste_x[i]) + 15,  height - float(liste_y[i])- 15,
                           float(liste_x[i]) + 19,  height - float(liste_y[i]) - 19,
                           fill="green")
    j = droite_regression(liste_x,liste_y)
    liste_tracer_droite.insert(0, j[1])
    liste_tracer_droite.insert(0, j[0])





# Série de test partie 1:

#creer_fichier_alea(50, "Fichier_alea")
#print(lit_fichier("Fichier_alea"))
# Les 2 tests si dessous s'éxécutent vers la fin du programme
#tk.Button(ecran, text="Graphique", command=lambda:print(trace_Nuage("Fichier_alea"))).grid()
#tk.Button(ecran, text="Trace_droite", command=lambda:(trace_droite(5, 4))).grid()

# Série de test partie 2
#print(moyenne([4, 6, 5, 6, 8, 4, 6, 5, 10, 5]))
#print(moyenne([7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(variance([7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(covariance([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(correlation([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(forteCorrelation([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(droite_reg([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))



# Programme Principale

# Constantes et Variables globale
width , height = 650, 650               # Taille de la fenêtre
liste = []
liste_couleur = ["green", "red", "yellow", "orange", "purple", "black", "pink"]
couleur = liste_couleur[randint(0, len(liste_couleur)-1)]
peut_tracer = True
liste_x, liste_y = [], []
dessin = False
liste_tracer_droite = [randint(0, 3), randint(5, width)]
nombre_choisi = 0




# Création de la fenêtre
ecran = tk.Tk()
ecran.geometry("666x666")
ecran.title("Projet Statistiques descriptive à deux variables: droite de régression.")
ecran.config(bg="grey")


menubar = tk.Menu(ecran)
ecran.config(menu=menubar)

menuf = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menuf)
menuf.add_command(label= "Sauvegarder", command=sauvegarde_configuration)
menuf.add_command(label="récupération_Sauvegarde", command=recuperer_configuration)
menuf.add_command(label="Aide", command=aide)
menuf.add_command(label="Quitter", command=ecran.quit)


menud = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Dessin", menu=menud)
menud.add_command(label= "Activer", command=activer)
menud.add_command(label= "Désctiver", command=desactiver)

menus = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="droite de régréssion", menu=menus)
menus.add_command(label="tracer", command=lambda:(trace_droite(liste_tracer_droite[0],liste_tracer_droite[1])))
menus.add_command(label="Changer couleur", command=changer_couleur)





canvas = tk.Canvas(ecran, bg="white", width=width, height=height)
canvas.grid(row=0 ,column=0, rowspan=18, pady=5, padx=5)

"""
tk.Button(ecran, text="Trace_droite correlation", command=lambda:(trace_droite(liste_tracer_droite[0],liste_tracer_droite[1])))\
    .grid(row=1 ,column=1, padx=50)

tk.Button(ecran, text="Autre couleur", command=changer_couleur).grid(row=2 ,column=1, padx=50)


tk.Button(ecran, text="Nuages de points: Fichier Alea", command=lambda:trace_Nuage("Fichier_alea")).grid(row=4 ,column=1, padx=50)
tk.Button(ecran, text="Nuages de points: Fichier exemple.txt", command=lambda:trace_Nuage("exemple.txt")).grid(row=5,column=1, padx=50)

tk.Button(ecran, text="Quitter", command=ecran.quit).grid(row=10,column=1)


tk.Button(ecran, text="villes_virgules.csv", command=extraire_info_fichier).grid(row=6,column=1)
tk.Button(ecran, text="anscombe.csv", command=extraire_info_fichier_2).grid(row=6,column=2)

# ajout des boutons pour activer et désaactiver la partie dessin
tk.Button(ecran, text="Activer", command=activer).grid(row=9, column=1)
tk.Button(ecran, text="Désactiver", command=desactiver).grid(row=9, column=2)

tk.Label(ecran, text="Entrez le nombre de points que vous voulez. Doit être différente de 0 :").grid(row=7, column=1)
entry = tk.Entry(ecran, bg="white", fg="red")
entry.grid(row=8, column=1)
tk.Button(ecran, text="Valider", command=valeur_entrer).grid(row=8, column=2)


tk.Button(ecran, text="Aide", command=aide).grid(row=10,column=2)
tk.Button(ecran, text="Sauvegarde", command=sauvegarde_configuration).grid(row=11,column=1)
tk.Button(ecran, text="récupération_Sauvegarde", command=recuperer_configuration).grid(row=11,column=2)
"""







canvas.bind("<Button>", ajout_point)
ecran.mainloop()



