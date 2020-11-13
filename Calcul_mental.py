import random
nb_utilisateur = 0
maxi = 200
premier_nombre = random.randint(1, 100)
deuxieme_nombre = random.randint(1, 100)


def demander_nombre_utilisateur(maxi):
    nb_utilisateur = input(f"Quel est le résultat de {premier_nombre}+{deuxieme_nombre}")
    try:
        nb_utilisateur = int(nb_utilisateur)
    except:
        print("Mettez un nombre s'il vous plait")
        demander_nombre_utilisateur(maxi)
    else:
        if nb_utilisateur > maxi:
            print("Votre nombre n'est pas dans la fourchette de nombre a trouvé")
            demander_nombre_utilisateur(maxi)

        return nb_utilisateur


while nb_utilisateur != (premier_nombre+deuxieme_nombre):
    nb_utilisateur = demander_nombre_utilisateur(maxi)
    if nb_utilisateur < (premier_nombre+deuxieme_nombre):
        print("Non se n'est pas sa , c'est plus grand")
    elif nb_utilisateur > (premier_nombre + deuxieme_nombre):
        print("Non se n'est pas sa , c'est plus petit")
    else:
        print("Vous avez gagné")

