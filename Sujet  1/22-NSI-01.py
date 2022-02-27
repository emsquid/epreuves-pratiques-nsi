def recherche(caractere: str, mot: str) -> int:
    """renvoie le nombre d'occurences du caractere dans le mot"""
    assert type(caractere) == type(mot) == str, "caractere et mot doivent etre des str"
    # solution facile : mot.count(caractere)
    compte = 0
    for lettre in mot:
        if lettre == caractere:
            compte += 1
    return compte


Pieces = [100, 50, 20, 10, 5, 2, 1]


def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution  # on retourne la solution quand on n'a plus rien a rendre
    p = Pieces[i]
    if p <= arendre:  # si la piece est plus petite que a rendre
        solution.append(p)  # on l'ajoute a la solution
        return rendu_glouton(arendre - p, solution, i)
    else:
        # sinon on passe a la piece suivante
        return rendu_glouton(arendre, solution, i + 1)
