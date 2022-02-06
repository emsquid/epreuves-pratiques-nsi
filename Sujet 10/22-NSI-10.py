def occurences_lettres(phrase: str) -> dict:
    """renvoie un dictionnaire contenant
    le nb d'occurences des caracteres de la phrase"""
    assert type(phrase) == str, "la phrase doit etre une chaine de caracteres"
    dico = dict()  # on initialise un dico vide
    for lettre in phrase:
        # on essai de recuperer le nombre d'occurences, sinon on initialise a 0
        # puis on incremente de 1
        dico[lettre] = dico.get(lettre, 0) + 1
    return dico


def fusion(L1, L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:  # tant que i1 < n1 et i2 < n2
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]  # on ajoute L1[i1] s'il est plus petit
            i1 = i1 + 1  # on incremente i1
        else:
            L12[i] = L2[i2]  # sinon on ajoute L2[i2]
            i2 = i2 + 1  # on incremente i2
        i += 1
    # quand une des deux listes est vide on vide l'autre
    while i1 < n1:
        L12[i] = L1[i1]
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        L12[i] = L2[i2]
        i2 = i2 + 1
        i = i + 1
    return L12
