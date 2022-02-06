def recherche(tab: list, n: int) -> int:
    """renvoie l'indice de n dans tab ou -1 (par recherche dichotomique)"""
    assert type(tab) == list and len(tab) > 0, "tab doit etre un tableau non vide"
    debut, fin = 0, len(tab) - 1  # bornes de la recherche
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tab[milieu] == n:
            return milieu
        elif tab[milieu] < n:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def position_alphabet(lettre):
    return ALPHABET.find(lettre)


def cesar(message, decalage):
    resultat = ""
    for lettre in message:
        if lettre in ALPHABET:  # si la lettre est dans l'alphabet
            indice = (position_alphabet(lettre) + decalage) % 26  # on code la lettre
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + lettre  # sinon on ajoute juste la lettre
    return resultat
