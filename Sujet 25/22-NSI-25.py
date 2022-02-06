def selection_enclos(table_animaux: list, num_enclos: int) -> list:
    """renvoie une table contenant les enregistrements dont l'enclos est num_enclos"""
    # par comprehension, on pourrait decomposer les etapes
    return [enreg for enreg in table_animaux if enreg["enclos"] == num_enclos]


def trouver_intrus(tab, g, d):
    """
    Renvoie la valeur de l'intrus situé entre les indices g et d
    dans la liste tab où
    tab vérifie les conditions de l'exercice,
    g et d sont des multiples de 3.
    """
    if g == d:
        return tab[g]  # on renvoie l'intrus
    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        # on verifie si l'indice et son voisin sont egaux
        if tab[indice] == tab[indice + 1]:  # on est strictement avant l'intrus
            return trouver_intrus(tab, indice + 3, d)  # la gauche devient indice + 3
        else:  # sinon on est apres l'intrus
            return trouver_intrus(tab, g, indice)  # la droite devient l'indice
