from math import sqrt   # import de la fonction racine carree

def distance(point1, point2): 
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((...)**2 + (...)**2)

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant a la plus     
    courte distance du point depart."""
    point = tab[0]
    min_dist = ...
    for i in range (1, ...):
        if distance(tab[i], depart)...:
            point = ...
            min_dist = ...
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"
