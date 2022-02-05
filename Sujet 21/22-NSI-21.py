def multiplication(n1: int, n2: int) -> int:  # identique au sujet 19
    """renvoie le produit de n1 par n2"""
    assert type(n1) == type(n2) == int, "n1 et n2 doivent etre des entiers"
    if n2 == 0:  # 0 * n1 = 0 dans tous les cas
        return 0
    elif n2 > 0:  # si n2 est positif on renvoie n1 + le produit de n1 par (n2 - 1)
        return n1 + multiplication(n1, n2 - 1)
    else:  # si n2 est negatif on change les signes
        return multiplication(-n1, -n2)


def dichotomie(tab, x):
    """La fonction renvoie True si tab contient x et False sinon"""
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2  # milieu
        if x == tab[m]:
            return True  # on a trouve
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1  # x < tab[m], on reduit l'intervalle a [debut, milieu - 1]
    return False  # on n'atteint ce return si x n'est pas dans le tableau
