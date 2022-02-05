def moyenne(tab: list) -> float:  # similaire au sujets 28 et 35
    """renvoie la moyenne du tableau"""
    assert type(tab) == list and tab != [], "tab doit etre un tableau non vide"
    # solution facile : return sum(tab) / len(tab)
    total = 0
    for element in tab:
        total += element
    return total / len(tab)


coeur = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def affiche(dessin):
    '''affichage d'une grille : les 1 sont repreente par
    des "*" , les 0 par deux espaces "  "'''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end="")
            else:
                print("  ", end="")
        print()


def zoomListe(liste_depart, k):
    """renvoie une liste contenant k fois chaque
    element de liste_depart"""
    liste_zoom = []  # liste_zoom initialisee vide
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)  # on ajoute k fois l'elt
    return liste_zoom


def zoomDessin(grille, k):
    """renvoie une grille ou les lignes sont zoomees k fois
    ET repetees k fois"""
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)  # on cree la ligne zoomee
        for i in range(k):
            grille_zoom.append(liste_zoom)  # on ajoute k fois la liste zoome
    return grille_zoom
