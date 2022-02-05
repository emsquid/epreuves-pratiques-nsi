from math import sqrt  # import de la fonction racine carree


def recherche(tab: list, n: int) -> int:  # similaire au sujet 32
    """renvoie  l'indice  de  la  dernière  occurrence  de
    l'élément  cherché, la taille du tableau s'il n'y est pas"""
    assert type(tab) == list and tab != [], "tab doit etre un tableau non vide"
    reponse = len(tab)  # on initialise la reponse a la longueur du tableau
    for i in range(len(tab)):
        if tab[i] == n:
            reponse = i
    return reponse


def distance(point1, point2):
    """Calcule et renvoie la distance entre deux points."""
    assert type(point1) == type(point2) == tuple, "les points doivent etre des tuples"
    assert len(point1) == len(point2) == 2, "les points doivent avoir 2 coordonnees"
    # formule de la distance
    return sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"


def plus_courte_distance(tab, depart):
    """Renvoie le point du tableau tab se trouvant a la plus
    courte distance du point depart."""
    assert type(tab) == list, "tab doit etre un tableau de tuples"
    point = tab[0]
    min_dist = distance(point, depart)  # on initialise la distance minimum
    for i in range(1, len(tab)):  # on parcourt tout le tableau
        if distance(tab[i], depart) < min_dist:  # si la distance est inferieur a min
            point = tab[i]  # on change le point associe
            min_dist = distance(tab[i], depart)  # et la distance
    return point


assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"
