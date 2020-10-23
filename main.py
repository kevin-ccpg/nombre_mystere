
"""
Jeu console Python: Le nombre mystère
Objectif : Le joueur doit trouver le nombre mystère avec le moins de coups possible.

Spécifications :
Le nombre mystère est un nombre généré aléatoirement compris entre une valeur min et une valeur max.
Un coup = Un essai. A chaque nombre entré par le joueur, lui indiquer si c'est plus ou si c'est moins que le nombre mystère
Indiquer au joueur le nombre de fois qu'il a tenté (coup) avant de trouver le nombre mystère.
Trois choix de niveau de difficulté seront proposé au joueur : 
  -> débutant : nombre aléatoire compris entre 1 et 100
  -> intermediaire : nombre aléatoire compris entre 1 et 1000
  -> expert : nombre aléatoire compris entre 1 et 10000
A la fin de chaque partie, le script propose au joueur de recommencer une partie. Et ainsi de relancer le jeu.
Si le joueur ne souhaite pas rejouer, le programme se ferme.

Bonus : Si l'utilisateur rentre une valeur qui n'est pas comprise entre 1 et la valeur max (selon niveau de difficulté), 
ou si il rentre une chaine de caractère au lieu d'un nombre pendant la partie, lui indiquer que cette valeur ne correspond pas au jeu.
Il faut donc ne pas le compter comme un coup et lui reposer la question jusqu'à ce que cette valeur soit correcte.


Notions utilisées pour le jeu : Variables, Boucles, Conditions, Fonctions
"""
