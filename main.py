"""
Jeu ou le joueur doit affronter des monstre et perd des PV en fonction des action qu'il fait.
par: Elliot Belair
groupe: 407
"""

import random

noms_monstres = ["gobelin", "loup", "dragon"]
force_monstres = [2, 4, 8]
pv = 20
tour = 0

def afficher_etat():
    global pv
    global tour
    print(f"Vous avez {pv} points de vie restant et vous êtes rendu au tour {tour}.")



def combattre():
    global pv
    """Génère la force du monstre et retire des PV."""
    monstre = random.choice(noms_monstres)
    print(f"Vous rencontrez un {monstre}.")
    victoire = random.randint(1,10)
    if victoire >= 6 :
        pv_change = force_monstres[noms_monstres.index(monstre)]
        pv += pv_change
        print(f"Vous gagnez la bataille. +{pv_change} PV ")
    elif victoire <= 5 :
        pv_change = force_monstres[noms_monstres.index(monstre)]
        pv -= pv_change
        print(f"Vous perdez la bataille. -{pv_change} PV ")
    return pv


def eviter():
    global pv
    monstre = random.choice(noms_monstres)
    pv -= 2
    print(f"Vous  avez évité un {monstre}. -2 PV ")
    return pv


def afficher_regles():
    print("regle")




while pv > 0 and tour < 10:
    choix = input("Combattre (C), éviter (E) ou règles (R) ? ")
    if choix == "C" :
        tour += 1
        combattre()
        afficher_etat()
    elif choix == "E":
        tour += 1
        eviter()
        afficher_etat()
    elif choix == "R":
        afficher_regles()
    else:
        print("Commande non reconue")


if pv <= 0 :
    print("Vous êtes mort.")
elif tour == 10 :
    print(f"Vous avez gagné avec {pv} PV restant.")
