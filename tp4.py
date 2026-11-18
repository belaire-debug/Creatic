"""
Par: Elliot Belair, Groupe:407
Jeu de combat de monstres en utilisant la POO.
"""

import random


NOMS_MONSTRES = ["gobelin", "loup", "dragon"]


class Monstre:
    """Représente un monstre avec un nom et une force."""
    def __init__(self, nom, force):
        self.nom = nom
        self.force = force


def creer_monstre_aleatoire():
    """Crée un monstre avec un nom et une force choisis au hasard."""
    nom = random.choice(NOMS_MONSTRES)
    force = random.randint(1, 8)
    return Monstre(nom, force)


class Heros:
    """Représente le héros et gère ses points de vie."""
    def __init__(self):
        self.pv = 20
        self.tour = 0
        self.monstres_vaincus = 0
        self.monstres_evites = 0
        self.defaites = 0

    def combattre(self, monstre):
        """Fait combattre le héros contre un monstre."""
        print(f"Vous rencontrez un {monstre.nom}.")
        victoire = random.randint(1, 10)
        if victoire >= 6:
            pv_change = monstre.force
            self.pv += pv_change
            self.monstres_vaincus += 1
            print(f"Vous gagnez la bataille. +{pv_change} PV ")
        elif victoire <= 5:
            pv_change = monstre.force
            self.pv -= pv_change
            self.defaites += 1
            print(f"Vous perdez la bataille. -{pv_change} PV ")

    def eviter(self, monstre):
        """Le héros évite le monstre et subit une pénalité fixe."""
        self.pv -= 2
        self.monstres_evites += 1
        print(f"Vous avez évité un {monstre.nom}. -2 PV ")

    def afficher_etat(self):
        """Affiche les PV actuels et le numéro du tour."""
        print(f'PV: {self.pv}')
        print(f'Tour: {self.tour}')
        print(f'Montre vaincus: {self.monstres_vaincus}')
        print(f'Montre evites: {self.monstres_evites}')
        print(f'Defaites: {self.defaites}')

    def est_vivant(self):
        """Retourne True si le héros a encore des PV."""
        return self.pv > 0


def afficher_regles():
    """Affiche les règles du jeu."""
    print("regle")


hero = Heros()


def game():
    while hero.est_vivant() and hero.tour < 10:
        choix = input("Combattre (c), éviter (e) ou règles (r)? ")
        if choix == "c":
            monstre = creer_monstre_aleatoire()
            hero.combattre(monstre)
            hero.tour += 1
            hero.afficher_etat()
        elif choix == "e":
            monstre = creer_monstre_aleatoire()
            hero.eviter(monstre)
            hero.tour += 1
            hero.afficher_etat()
        elif choix == "r":
            afficher_regles()


def end():
    if hero.est_vivant():
        print(f"Vous avez gagne la partie avec {hero.pv} PV")
    elif not hero.est_vivant():
        print(f"Vous avez perdu la partie avec {hero.pv} PV.")
        print(f"Vous avez survecu {hero.tour} tours.")


def replay():
    rejouer = input(f"Voulez-vous rejouer. (y/n)")

    if rejouer == "y":
        hero.monstres_vaincus = 0
        hero.monstres_evites = 0
        hero.defaites = 0
        hero.pv = 20
        hero.tour = 0
        game()
        end()
        replay()
    elif rejouer == "n":
        print("Merci d'avoir joue")
    else:
        print("La reponse n'est pas reconu.")
        replay()


game()
end()
replay()
