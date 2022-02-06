from typing import Any


def recherche(a: Any, t: list) -> int:
    """renvoie le nombre d'occurences de a dans t"""
    assert type(a) == float or type(a) == int, "a doit etre un nombre"
    assert type(t) == list, "t doit etre un tableau"
    # solution facile : return t.count(a)
    compte = 0
    for element in t:
        if element == a:
            compte += 1
    return compte


def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []  # on initialise une liste vide
    a_rendre = s_versee - s_due
    i = len(pieces) - 1
    while a_rendre > 0:  # tant qu'il reste de l'argent a rendre
        if pieces[i] <= a_rendre:
            rendu.append(pieces[i])  # on ajoute la piece au rendu
            a_rendre = a_rendre - pieces[i]  # et on retire sa valeur
        else:
            i = i - 1  # sinon on prend une piece de valeur moins elevee
    return rendu
