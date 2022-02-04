def recherche(tableau:list)->list:
    """renvoie la liste des eventuels couple d'entiers consécutifs dans tab"""
    couples = []
    for i in range(len(tableau) - 1): # on s'arrete avant le dernier car il n'a pas de suivant
        actuel, suivant = tableau[i], tableau[i + 1]
        if (suivant - actuel) == 1: # si (suivant - actuel) == 1 ils sont consecutifs
            couples.append((actuel, suivant)) # on ajoute le couple
    return couples

def propager(M, i, j, val):
    if M[i][j] == 0: # si le pixel vaut 0 on ne fait rien
        return

    M[i][j] = val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1): # si l'element vaut 1
        propager(M, i-1, j, val)

    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1): # i + 1 : element en bas 
        propager(M, i+1, j, val) # on propage a i + 1

    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1): # j - 1 : element a gauche
        propager(M, i, j-1, val) # on propage a j - 1

    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1): # j + 1 : element a droite
        propager(M, i, j+1, val) # on propage a j + 1
