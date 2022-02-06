def recherche(elt: int, tab: list) -> int:
    """retourne l'indice de la premiere occurence de elt dans tab ou -1"""
    assert type(tab) == list, "tab doit etre une liste"
    for i in range(len(tab)):
        if tab[i] == elt:
            return i  # on retourne des que l'on trouve elt
    return -1


def insere(a, tab):
    l = list(tab)  # l contient les mêmes éléments que tab
    l.append(a)
    i = len(l) - 2  # indice de l'avant derniere valeur
    # tant que la valeur precedant a est plus grande et que i >= 0
    while a < l[i] and i >= 0:
        # on echange a et la valeur precedente
        l[i + 1] = l[i]
        l[i] = a
        i = i - 1
    return l
