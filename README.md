# Projet Statistiques descriptive à deux variables: droite de régression. 

Informations: 
    - Licence Mathématiques Informatique TD04 
    - Groupe N ° 06
    - Réalisé par: 
        * Lilian SOMMY 22106064
        * Mathis VISBECQ 22103193
        * Alann MONNIER-BLONDEAU 22102829
    - URL Projet:
        * https://github.com/alann22102829/projet_stat_A_L_M.git
    - Nom des fichiers:
        | Fichier principale:
            *
        | Fichier csv:
            * villes_virgules.csv
        | Fichier texte:
            * exemple.txt
        | Fichier supplémentaire:
            * Readme


Répartitionn travail:
    - Lilian SOMMY: 
        # Gestion du dépôt Github
        # Création fonction partie 2
        # Explication de la partie 2
        # Aide partie 3
        # Bonus
    - Mathis VISBECQ:
        # Gestion de la mise en forme (règles de style PEP8, respect pratique programmation, fautes orthographes)
        # Création de la partie 1
        # Explication de la partie 1
        # Bonus
    - Alann MONNIER-BLONDEAU:
        # Création de la partie 3 
        # Explication de la partie 3
        # Mise en page du README
        # Bonus

Présentation du projet:

Introduction: Utilisation des statistiques descriptives à deux variables pour pouvoir créer une droite de régréssion. La statistique descriptive est une technique qui regroupe de nombreuse technique pour décrire un ensemble important de données. Ici nous utilisons la droite de régression qui est la droite que l'on trace grâce à un nuages de points et qui représente la distribution des deux caractères étudiés.

Bibliothèques utilisées:
    - Tkinter (Création de l'interface graphique pour afficher les nuages de points, la droite de régression ainsi que pour la création des boutons.)
    - Random (Utilisation des méthodes uniform() --> choisir nbr aleatoire flottant et randint --> choisir nbr aleatoire entier.)
    - Math (Utilisation de la méthode sqrt() --> pour pouvoir calculer la racine carré d'un nombre.)
    - Os (Peut interagir avec les fonctionnalités du système d'exploitation et accéder aux informations. Permet aussi de travailler avec les fichiers et répertoires du systèmes.)
    - Pandas (Permet de manipuler et analyser des données.)


Partie 1:
                                                Partie "Outils"

# explication des fonctions(ce qu elle font, les paramètres qu elles prennent, ce que ça retourne)
                                               Partie "Outils"
1)Fonction creer_fichier_alea(nb, nomfichier) : créer un fichier avec 500 coordonnés flottante aléatoire (en utilisant la méthode unfiorm de la bibliothèque random) x et y qui vont de 0 à 500. nb représente le nombre de ligne qu'on shouaite ajouter dans nomFichier.  


2)Fonction lit_fichier(nomfic) : lit les coordonnés de chaque ligne qu'il y a dans le fichier qu'on a créer dans la fonction creer_fichier_alea(nb, nomfichier).


3)Fonction trace_Nuage(nomf) : appelle plusieurs variables global height qui récupere la hauteur de la 
fenetre, liste_y et liste_x qui récupère les coordonnees du fichier_alea et aussi liste_tracer_droite qui va récupérer le coefficient directeur(a) et l'ordonée à l'origine (b). 
Cette fonction  place des point sur un canevas en utilisant les coordonnés que l'on crée avec la focntion creer_fichier_alea(nb, nomfichier).


4)Fonction trace_droite(a, b) : appelle plusieurs variables global height qui recupere la hauteur de la 
fenetre, width qui recupere la largeur de la fenetre, couleur qui recupere la couleur choisi,
liste qui récupère la variable qui représente la ligne tracé pour pouvoir la supprimer plus facilement dans d'autres fonctions.peut_tracer renvoie le booleen qui nous permé de savoir si on peut tracer la droite ou 
non, liste_x et liste_y renvoie les coordonnees du fichier_alea.
Calcule si la corrélation est forte grâce à  forteCorrelation() qui renvoie True ou False. Si  True la fonction trace_droite(a,b) trace la droite de corrélation.


5)Fonction tracer_axes() : cette fonction cree les axes des abcisse et des ordonnees avec les graduations 
representer par des barres toutes les 50 unitées.


# bien parler du fichier qu on va créer
Explication des tests:



                                                Partie " Calculs Statistiques"

# explication des fonctions(ce qu elle font, les paramètres qu elles prennent, ce que ça retourne)
Pour la partie de caluls de statistique il est nécessaire d'avoir ces 4 outils definit :

"moyenne(serie)"

C'est une fonction qui prends en entrée une liste et calculs la moyenne des flottant qu'elle contient.

Cette fonction renvoie donc un flottant.

"variance(serie)"

C'est une fonction qui prends en entrée une liste et en calculs la variance a l'aide de l'outils moyenne() en suivant cette équation:

![image](https://user-images.githubusercontent.com/91246964/167264923-efe9ffa2-a3d9-4e29-8adb-8a803fbd8adb.png)

Cette fonction renvoie donc un flottant.

"covariance(serieX, serieY)"
Prends en entrée deux listes (ici correspondant aux coordonnée x et y) pour a l'aide de l'outils variance() en calculer la covariance en suivant cette équation:

![image](https://user-images.githubusercontent.com/91246964/167264980-cf1b1d43-48ed-4fcd-8e1e-dfa89e438426.png)

Cette fonction renvoie donc un flottant.


"correlation(serieX, serieY)"

Fonction qui prends en entrée deux listes pour en calculer, a l'aide de l'outils "variance()" le coefficient de correlation en suivant cette équation:

![image](https://user-images.githubusercontent.com/91246964/167265085-dbb71a89-6e78-40cd-bdde-f6e21215bde4.png)

Cette fonction renvoie donc un flottant.

Voiçi les fonction utiliser pour la partie calculs en statistique:

Afin de savoir si il est pertinent de tracer une droite de regression il faut que le coefficient de correlation sois compris en dehors de -0.8 et 0.8

la fonction "forteCorrelation(serieX, serieY)" verifie cela.

La fonction droite_regression(serieX, serieY) elle permet grace aux outils covariance() et moyenne() de renvoiyer deux flottant correspondant au coefficient directeur (a) et l'ordonnée a l'origine (b) de la droite de regression qui est de forme y = ax+b 

![image](https://user-images.githubusercontent.com/91246964/167265454-30f8ecc7-2f73-4df8-b7b5-cc0fd306ba31.png)


La fonction "aide()" renvoie vers ce Readme





                                                Programme Principale

Création d'une fenêtre nomée ecran de taille 1250x666 avec comme titre "Projet Statistiques descriptive à deux variables: droite de régression.".
Création d'un canvas avec une taille défini grâce à deux constantes height et weight. 
    
    1) Button "tracer_droite correlation" utilise la fonction présenter dans la partie "Outils" du Readme va donc tracer la 
    droite de correlation d'un nuages de points ou tracer une droite avec des coordonées aléatoires si on a pas de nuages de points.
    
    2) Button " Autre_couleur" va changer la couleur de la droite la prochaine fois qu'on appuie sur le bouton tracer droite.
    Appelle la fonction changercouleur détaillé après. 
    
    3) Création de deux boutons Nuages de points avec deux fichier différents. Va tracer le nuage de points en utilisant les deux
    fichiers et en appelant la fonction trace_Nuage(filename). 
    
    4) Bouton "Quitter" qui va fermer la fenêtre lorsqu'on clique dessus grâce à la méthode ecran.quit.
    
    5) Création de deux autres boutons avec le nom de deux fichiers csv qui vont afficher le nuage de point de ces deux fichiers.
    Les deux fonctions sont quasiement similaire mais on en as fait deux pour plus de lisibilité et pour éviter d'avoir beaucoup 
    d'argument dans la fonction. 
    
    6) Une entrée et un bouton valider pour entrer le nombre de ligne que l'utilisateur veut et le valider grâce aux boutons.  
    
    7) Deux boutons actver et désactiver. Si l'on appuie sur activer on peut ajouter des points sur le canvas qui sont pris en compte 
    dans le calcul de la corrélation. Et si on fait désactiver on ne peut plus en ajouter. 
Il est a noté que les boutons decrit ci dessus sont placer dans des Menus.
Explication des fonctions:
    
    1) Fonction trace_droite expliqué dans la partie "Outil"
    
    2) Fonction changer_couleur() : Appelle deux variables globales couleur qui va récupérer la couleur choisi. Et liste couleur qui
    contient 7 couleurs. On va récupérer une couleur dans la liste en choisissant un indice aléatoirement. On va importer la bibliothèque 
    random et utiliser la fonction randint qui retourne un nombre entier aléatoirement entre deux valeurs. 
    
    3) Fonction trace_Nuage(nomF) déjà expliqué dans la partie "Outil".
    
    4) Fonction activer() : Va appeler la variable globale dessin qui va être à fausse par défaut pour la mettre à vrai.
    
    5) Fonction désactiver() : Va appeler la variable globale dessin pour la mettre à fausse.
    
    6) Les 2 fonctions précédantes sont reliés par la méthode canvas.bind("<Button>", ajout_point) et la fonction ajout_point(). Dès que l'on 
	clique dans le canvas va appeler cette fonction. Cette fonction prend comme argument event qui représente l'évènement clic et qui est 
	obligatoire avec la méthode bind(). 
    Appelle 4 variables globales les deux listes de coordonées x et y, une liste qui contient les variables ligne que l'on a tracé ainsi que 
	la variable dessin qui si elle est a false ne trace pas les points. Si dessin a True. On créer un point en utilisant les coodonées récupérés
	grâce à event.x et event.y qui donne les coordonnées ou l'on clique. Ensuite ajoute les coordonnées dans les deux listes de coordonnées.
    On ne peut tracer la droite de corrélation que si l'on a deux points si c'est le cas on récupère les variables a et b grâce à
	fonction droite_reg(liste_x, liste_y) et on les ajoute dans la liste "liste_tracer_droite".
    
    7) Fonction extraire_info_fichier() : Va lire le fichier csv grâce à la bibliothèque panda et la méthode pandas.read_csv(). 
    Ensuite on récupère les lignes et colones qu'on veut en imposant que la pop de chaque ville est inférieur à 500 pour les populations de 2010 et 2012.
	Ensuite grâce à la méthode .tolist() (que l'on a découvert en demandant à un de nos amis car on ne trouvais pas comment juste récupérer les valeurs 
	d'une colone) on récupère les valeurs d'une colone.
    On entre ensuite ses données dans un fichier texte puis on lit ce fichier et trace le nuage de point des habitants de 2010 en fonction des habitants de 2012. 
    
    8) Fonction extraire_info_fichier_2(): Même utilisation que la fonction précédante sauf qu'on ne lit pas le même fichier. Récupère les donnée dans le fichier anscombe.csv qui sont des coordonées et qui vont nous permetrent de tracer une droite de corrélation de coordonnées de Y en fonction de X. 
    
    9) Fonction valeur_entry() : affecte à la variable gloabal le nombre_choisi, le nombre entré par l'utilisateur. 




                                                Bonus 

# explication des fonctions(ce qu elle font, les paramètres qu elles prennent, ce que ça retourne)
    1) sauvegarde_configuration() : appelle deux variables globales liste_x et liste_y qui récupère les coordonnees du 
fichier_alea. Cette fonction sauvegarde les coordonnees des points dans un fichier pour pouvoir les 
récupérer plus tard.
    
    2) recuperer_configuration() : appelle les deux même variables globales que sauvegarde_configuration().
Récupere les coordonnees dans le fichier, utilise tracer_axes() pour tracer les axes puis place les points 
au même endroit en leur mettant une couleur verte. 

# remplir dans le srcipt les docstring
Explication des tests:


Conclusion: 
    - Nombres de lignes pour le projet: 
    - Temps passé sur le projet: 11 heures + 24h derecherche d'un fichier CSV
