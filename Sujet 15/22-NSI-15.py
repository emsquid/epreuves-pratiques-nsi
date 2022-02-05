def nb_repetitions(elt, tab:list)->int:
    """renvoie le nombre d'occurences d'elt dans tab"""
    assert type(tab) == list, "tab doit etre une liste"
    # solution facile : return tab.count(elt)
    compte = 0
    for e in tab:
        if e == elt:
            compte += 1
    return compte
    

def binaire(a):
    bin_a = str(a%2) # on ajoute le premier bit 
    a = a // 2
    while a > 0:
        bin_a = str(a%2) + bin_a # on ajoute les bits suivants devant
        a = a // 2 # on effectue la divison euclidienne de a par 2
    return bin_a
