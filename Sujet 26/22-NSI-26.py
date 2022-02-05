def rechercheMin(tab: list) -> int:
    """renvoie l'indice de la premiere occurence du minimum de tab"""
    assert type(tab) == list and tab != [], "tab doit etre un tableau non vide"
    i_min = 0
    for i in range(len(tab)):
        if tab[i] < tab[i_min]:
            i_min = i
    return i_min


def separe(tab):  # identique au sujet 12
    i = 0
    j = len(tab) - 1
    while i < j:
        if tab[i] == 0:
            i = i + 1
        else:
            tab[i], tab[j] = tab[j], tab[i]
            j = j - 1
    return tab
