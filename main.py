import random
import tkinter
from tkinter import *
from tkinter import messagebox
"""
Jeu console Python: Le nombre mystère
Objectif : Le joueur doit trouver le nombre mystère avec le moins de coups possible.

Spécifications :
Le nombre mystère est un nombre généré aléatoirement compris entre une valeur min et une valeur max.
Un coup = Un essai. A chaque nombre entré par le joueur, lui indiquer si c'est plus ou si c'est moins que le nombre
mystère
Indiquer au joueur le nombre de fois qu'il a tenté (coup) avant de trouver le nombre mystère.
Trois choix de niveau de difficulté seront proposé au joueur : 
  -> débutant : nombre aléatoire compris entre 1 et 10
  -> intermediaire : nombre aléatoire compris entre 1 et 100
  -> expert : nombre aléatoire compris entre 1 et 1000
A la fin de chaque partie, le script propose au joueur de recommencer une partie. Et ainsi de relancer le jeu.
Si le joueur ne souhaite pas rejouer, le programme se ferme.

Bonus : Si l'utilisateur rentre une valeur qui n'est pas comprise entre 1 et la valeur max (selon niveau de difficulté), 
ou si il rentre une chaine de caractère au lieu d'un nombre pendant la partie, lui indiquer que cette valeur ne 
correspond pas au jeu.
Il faut donc ne pas le compter comme un coup et lui reposer la question jusqu'à ce que cette valeur soit correcte.


Notions utilisées pour le jeu : Variables, Boucles, Conditions, Fonctions
"""


# Initialisation de TKinter
mainapp = tkinter.Tk()

# Création de la fenêtre
mainapp.title("Nombre Mistère")
mainapp.geometry("800x600")
mainapp.configure(bg='red')
mainapp.resizable(width=False, height=False)

nb_mystere = 0


def nombreMystere(niveau):
    maxi = 0
    if niveau == 1:
        print("Vous avez choisi la difficulté facile")
        maxi = 10
    if niveau == 2:
        print("Vous avez choisi la difficulté intermediaire")
        maxi = 100
    if niveau == 3:
        print("Vous avez choisi la difficulté difficile")
        maxi = 1000

    global nb_mystere
    nb_mystere = random.randint(1, maxi)
    print("nb_mystere   ---- >" + str(nb_mystere))


def effacer():
    saisie_nombre.delete(0, END)


def show_about():
    about_window = tkinter.Toplevel(mainapp)
    about_window.title("A propos de")
    about_window.minsize(640, 480)
    about_window.maxsize(1280, 720)
    lb = tkinter.Label(about_window, text="Développer par Maxime Bouhier 2020")
    lb.pack()


# Creation du menu
mainmenu = tkinter.Menu(mainapp)
first_menu = tkinter.Menu(mainmenu)
first_menu.add_command(label="Quit", command=mainapp.quit)
first_menu.add_command(label="Rejouer", command=effacer)
second_menu = tkinter.Menu(mainmenu)
second_menu.add_command(label="Niveau 1", command=lambda: nombreMystere(1)) # Synthaxe pour TKinter pour passer des paramètres a une fonction
second_menu.add_command(label="Niveau 2", command=lambda: nombreMystere(2))
second_menu.add_command(label="Niveau 3", command=lambda: nombreMystere(3))
first_menu.add_command(label="A propos", command=show_about)
mainmenu.add_cascade(label="Menu", menu=first_menu)
mainmenu.add_cascade(label="Difficulté", menu=second_menu)
mainapp.config(menu=mainmenu)


def getEntry():
    result = entre_nombre.get()
    # Changement du label en fonction du nombre mystère
    if result < nb_mystere:
        var_label.set("C'est plus")
    elif result > nb_mystere:
        var_label.set("C'est moins")
    else:
        var_label.set("Gagné !!")

    return result


# Récupération du nombre saisie par l'utilisateur
entre_nombre = tkinter.IntVar()
saisie_nombre = tkinter.Entry(mainapp, textvariable=entre_nombre)

bouton_valid = tkinter.Button(mainapp, text="Validez", command=getEntry)

# Message qui indique à l'utilisateur si c'est plus ou moins
var_label = tkinter.StringVar()
var_label.set(getEntry())
label = tkinter.Label(mainapp, textvariable=var_label)

label.grid(row=0, column=2)
saisie_nombre.grid(row=0, column=0)
bouton_valid.grid(row=0, column=1)


mainapp.mainloop()


# continuer = True
# maxi = 0
#
#
# def demander_choix_niveau():
#     try:
#         print("1 pour facile")
#         print("2 pour intermediaire")
#         print("3 pour difficile")
#         nb_difficulte = input("Choisisez la difficulté :")
#         nb_difficulte = int(nb_difficulte)
#
#     except:
#         print("Merci de rentrer une valeur numérique")
#         demander_choix_niveau()
#     else:
#         if not 1 <= nb_difficulte <= 3:
#             print("Merci de rentrer une valeur entre 1 et 3")
#             demander_choix_niveau()
#
#         return nb_difficulte
#
#
# def demander_nombre_utilisateur(maxi):
#     nb_utilisateur = input("Donnez un nombre ")
#     try:
#         nb_utilisateur = int(nb_utilisateur)
#     except:
#         print("Mettez un nombre s'il vous plait")
#         demander_nombre_utilisateur(maxi)
#     else:
#         if nb_utilisateur > maxi:
#             print("Votre nombre n'est pas dans la fourchette de nombre a trouvé")
#             demander_nombre_utilisateur(maxi)
#
#         return nb_utilisateur
#
#
# while continuer:
#     # c'est ici que tu teste plutot si c'est 1 2 ou 3
#     nb_difficulte = demander_choix_niveau()
#
#     if nb_difficulte == 1:
#         print("Vous avez choisi la difficulté facile")
#         maxi = 10
#     if nb_difficulte == 2:
#         print("Vous avez choisi la difficulté moyenne")
#         maxi = 100
#     if nb_difficulte == 3:
#         print("Vous avez choisi la difficulté difficile")
#         maxi = 1000
#     nb_mistere = random.randint(1, maxi)
#
#     nb_vies = maxi
#     nb_utilisateur = 0
#     while nb_vies > 0 and nb_utilisateur != nb_mistere:
#         print(f"Vous avez {nb_vies} vies")
#         nb_utilisateur = demander_nombre_utilisateur(maxi)
#         if nb_utilisateur < nb_mistere:
#             print("Plus grand")
#             nb_vies -= 1
#         elif nb_utilisateur > nb_mistere:
#             print("Plus petit")
#             nb_vies -= 1
#         else:
#             print("Vous avez gagné")
#
#     if nb_vies == 0:
#         print("GAME OVER")
#
#     choix = input("Voulez vous continuer ?")
#     choix = choix.lower()
#     if choix != 'oui':
#         continuer = False
