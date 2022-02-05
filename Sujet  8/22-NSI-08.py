def recherche(elt: int, tab: list) -> int:
    """retourne l'indice de la premiere occurence de elt dans tab ou -1"""
    indice = -1  # on initialise l'indice a - 1
    for i in range(len(tab)):
        if tab[i] == elt:
            indice = i
    return indice


def insere(a, tab):
    l = list(tab)  # l contient les mêmes éléments que tab
    l.append(a)
    i = len(l) - 2  # indice de l'avant derniere valeur (avant a)
    # tant que la valeur precedent a est plus petite et que i >= 0
    while a < l[i] and i >= 0:
        # on echange a et la valeur precedente
        l[i + 1] = l[i]
        l[i] = a
        i = i - 1  # on decremente i
    return l
