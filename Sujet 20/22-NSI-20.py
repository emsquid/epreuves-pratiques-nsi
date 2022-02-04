def xor(a:list, b:list)->list:
    """renvoie a xor b"""
    assert type(a) == type(b) == list and len(a) == len(b), "a et b sont des tableaux de meme longueur"
    resultat = []
    for i in range(len(a)):
        resultat.append(a[i] ^ b[i]) # ^ : operateur xor en python
    return resultat


class Carre:
    def __init__(self, tableau = [[]]):
        self.ordre = len(tableau)
        self.valeurs = tableau
    
    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.valeurs[i])
    
    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        return sum(self.valeurs[i])
    
    def somme_col(self, j):
        '''calcule la somme des valeurs de la colonne j'''
        return sum([self.valeurs[i][j] for i in range(self.ordre)])

def est_magique(carre):
    n = carre.ordre
    s = carre.somme_ligne(0)
        
    #test de la somme de chaque ligne
    for i in range(1, n): # on va de 1 a n, la reference etant la ligne 0
        if carre.somme_ligne(i) != s:
            return False
        
    #test de la somme de chaque colonne
    for j in range(n):
        if carre.somme_col(j) != s: # on teste la somme de la colonne j
            return False
         
    #test de la somme de chaque diagonale (je conseille de visualiser dans sa tete)
    if sum([carre.valeurs[k][k] for k in range(n)]) != s: # premiere diago
            return False
    if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s: # deuxieme diago
            return False
    
    return True


