def taille(arbre: dict, lettre: str) -> int:
    """renvoie la taille de l'arbre qui a pour racine lettre"""
    if lettre == "":
        return 0
    else:
        taille_sag = taille(arbre, arbre[lettre][0])
        taille_sad = taille(arbre, arbre[lettre][1])
        return 1 + taille_sag + taille_sad


def tri_iteratif(tab):
    for k in range(len(tab) - 1, 0, -1):  # parcourt le tableau de la fin au debut
        imax = 0  # on cherche le max dans l'intervalle [0, k]
        for i in range(0, k):  # on parcourt le tableau du debut a k
            if tab[i] > tab[imax]:
                imax = i
        if tab[imax] > tab[k]:
            tab[k], tab[imax] = tab[imax], tab[k]  # on echange
    return tab
