def convertir(T: list) -> int:
    """
    T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
    représentant un entier écrit en binaire. Renvoie l'écriture
    décimale de l'entier positif dont la représentation binaire
    est donnée par le tableau T
    """
    entier = 0
    puissance = 0
    for bit in reversed(T):
        entier += (2**puissance) * bit  # * bit permet d'ajouter quand le bit vaut 1
        puissance += 1
    return entier


def tri_insertion(L):
    n = len(L)

    # cas du tableau vide
    if n == 0:
        return L

    for j in range(1, n):
        e = L[j]
        i = j

        # A l'etape j, le sous-tableau L[0,j-1] est trie
        # et on insere L[j] dans ce sous-tableau en determinant
        # le plus petit i tel que 0 <= i <= j et L[i-1] > L[j].
        while i > 0 and L[i - 1] > L[j]:
            i = i - 1

        # si i != j, on decale le sous tableau L[i,j-1] d'un cran
        # vers la droite et on place L[j] en position i
        if i != j:
            for k in range(j, i, -1):
                L[k] = L[k - 1]
            L[i] = e
    return L
