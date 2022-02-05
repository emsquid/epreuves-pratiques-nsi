from random import randint


def tri_selection(tab: list) -> list:
    """renvoie le tableau trie par ordre croissant"""
    for i in range(len(tab) - 1):
        i_min = i
        for j in range(i, len(tab)):
            if tab[j] < tab[i_min]:
                i_min = j
        tab[i], tab[i_min] = tab[i_min], tab[i]
        print(tab)
    return tab


def plus_ou_moins():
    nb_mystere = randint(1, 99)  # nombre entre 1 et 99 compris
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1  # on initialise le compteur a 1

    # tant qu'on n'a pas trouve et qu'on est a 10 essais ou moins on continue
    while nb_mystere != nb_test and compteur < 11:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre etait ", nb_mystere)
