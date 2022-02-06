def moyenne(tab: list) -> float:
    """renvoie la moyenne du tableau s'il n'est pas vide, erreur sinon"""
    # assert type(tab) == list and tab != [], "tab doit etre un tableau non vide"
    if tab == []:
        return "erreur"  # peut etre vaudrait il mieux faire un assert ?
    else:
        return sum(tab) / len(tab)  # on renvoie la somme divise par le nb de notes


def tri(tab):
    # i est le premier indice de la zone non triee, j le dernier indice.
    # Au debut, la zone non triee est le tableau entier.
    i = 0
    j = len(tab) - 1
    while i != j:
        if tab[i] == 0:
            i = i + 1  # on incremente juste i
        else:
            valeur = tab[j]  # sinon on echange avec j
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1  # on decremente j
    return tab
