def moyenne(tab: list) -> float:  # identique au sujet 28
    """
    moyenne(list) -> float
    Entrée : un tableau non vide d'entiers
    Sortie : nombre de type float
    Correspondant à la moyenne des valeurs présentes dans le
    tableau
    """
    assert type(tab) == list and tab != [], "tab doit etre un tableau non vide"
    # solution facile : return sum(tab) / len(tab)
    total = 0
    for element in tab:
        total += element
    return total / len(tab)


def dichotomie(tab, x):
    """
    tab : tableau trie dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if tab == []:
        return False, 1

    # cas ou x n'est pas compris entre les valeurs extremes
    if (x < tab[0]) or (x > tab[-1]):
        return False, 2

    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2  # milieu
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3  # dernier cas renvoyant False (False, 3)