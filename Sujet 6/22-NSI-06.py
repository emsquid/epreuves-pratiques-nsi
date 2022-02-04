def maxi(tab:list)->tuple:
    """retourne le maximum de la liste et son indice"""
    i_max = 0
    for i in range(len(tab)):
        if tab[i] > tab[i_max]:
            i_max = i
    return (tab[i_max], i_max)


def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0 # on commence a l'indice 0
    trouve = False
    # tant que l'on peut comparer (i < n - g) et qu'on n'a pas trouve
    while i < n - g and trouve == False: 
        j = 0
        while j < g and gene[j] == seq_adn[i+j]: 
            j += 1 # passe a la lettre suivante du gene
        if j == g:
            trouve = True
        i += 1 # on incremente i
    return trouve
