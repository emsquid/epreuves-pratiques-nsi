def maxi(tab:list)->tuple: # identique au sujet au sujet 6 ???
    """retourne le maximum de la liste et son indice"""
    i_max = 0
    for i in range(len(tab)):
        if tab[i] > tab[i_max]:
            i_max = i
    return (tab[i_max], i_max)


def positif(T):
    T2 = list(T) # copie
    T3 = [] # pile vide
    while T2 != []:
        x = T2.pop() # on depile 
        if x >= 0: # si x >= 0
            T3.append(x) # on l'empile dans la pile auxiliaire
    T2 = [] # inutile
    while T3 != []:
        x = T3.pop()
        T2.append(x) # on rempile tout dans la copie de T
    print('T = ',T)
    return T2

