def occurences_lettres(phrase:str)->dict:
    """renvoie un dictionnaire contenant 
    le nb d'occurences des caracteres de la phrase"""
    dico = {} # on initialise un dico vide
    for lettre in phrase:
        # on essai de get le nombre, sinon on initialise a 0, puis on ajoute 1
        dico[lettre] = dico.get(lettre, 0) + 1 
    return dico

def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0 # a quoi sert cette variable i ?
    while i1 < n1 and i2 < n2 :
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 = i1 + 1
        else:
            L12[i] = L2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
    	L12[i] = L1[i1]
    	i1 = i1 + 1
    	i = i + 1
    while i2 < n2:
    	L12[i] = L2[i2]
    	i2 = i2 + 1
    	i = i + 1
    return L12
