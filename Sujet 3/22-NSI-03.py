def delta(tableau:list)->list:
    """renvoie le tableau compresse a la maniere du delta encoding"""
    assert len(tableau) > 0, "le tableau ne doit pas être vide"
    resultat = [tableau[0]]
    for i in range(1, len(tableau)):
        diff = tableau[i] - tableau[i - 1] # on calcule la difference entre l'entier et le precedent
        resultat.append(diff)
    return resultat


class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d
    
    def __str__(self):
        return str(self.valeur)
    
    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = "" # on initialise l'expression
    if e.gauche is not None: 
        s = s + expression_infixe(e.gauche) # on ajoute l'expression du SAG
    s = s + str(e) # on ajoute la valeur de la racine
    if e.droit is not None: # on check si le SAD existe
        s = s + expression_infixe(e.droit) # on ajoute l'expression du SAD
    if e.est_une_feuille(): # si e est une feuille, on renvoie juste l'expression
        return s
    return '('+ s +')'


