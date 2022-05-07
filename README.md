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

# bien parler du fichier qu on va créer
Explication des tests:



                                                Partie " Calculs Statistiques"

# explication des fonctions(ce qu elle font, les paramètres qu elles prennent, ce que ça retourne)
Voiçi les fonction utiliser pour la partie calculs en statistique:

Afin de savoir si il est pertinent de tracer une droite de regression il faut que le coefficient de correlation sois compris en dehors de -0.8 et 0.8

la fonction "forteCorrelation(serieX, serieY)" verifie cela.

La fonction droite_regression(serieX, serieY) elle permet grace aux outils covariance() et moyenne() de renvoiyer deux flottant correspondant au coefficient directeur (a) et l'ordonnée a l'origine (b) de la droite de regression qui est de forme ax+b 

La fonction aide renvoie vers ce Readme



# remplir dans le srcipt les docstring
Explication des tests:



                                                Programme Principale

# explication des fonctions(ce qu elle font, les paramètres qu elles prennent, ce que ça retourne)
# remplir dans le srcipt les docstring
Explication des tests:



                                                Bonus 

# explication des fonctions(ce qu elle font, les paramètres qu elles prennent, ce que ça retourne)
# remplir dans le srcipt les docstring
Explication des tests:


Conclusion: 
    - Nombres de lignes pour le projet: 
    - Temps passé sur le projet:
    - Avis personel sur le projet:
        * Lilian SOMMY:

        * Mathis VISBECQ:

        * Alann MONNIER-BLONDEAU:
