def multiplication(n1: int, n2: int) -> int:
    """renvoie le produit de n1 par n2"""
    assert type(n1) == type(n2) == int, "n1 et n2 doivent etre des entiers"
    if n2 == 0:  # 0 * n1 = 0 dans tous les cas
        return 0
    elif n2 > 0:  # si n2 est positif on ajoute n1 au produit de n1 par (n2 - 1)
        return n1 + multiplication(n1, n2 - 1)
    else:  # si n2 est negatif on change les signes
        return multiplication(-n1, -n2)


def chercher(T, n, i, j):
    if i < 0 or j >= len(T):
        print("Erreur")
        return None
    if i > j:
        return None
    m = (i + j) // 2  # on calcule le milieu
    if T[m] < n:  # si la valeur du milieu < n
        return chercher(T, n, m + 1, j)  # le debut devient le milieu
    elif T[m] > n:  # sinon si elle est > n
        return chercher(T, n, i, j - 1)  # la fin devient le milieu
    else:
        return m  # sinon on a trouve
