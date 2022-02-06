def delta(tab: list) -> list:
    """renvoie le tableau compresse a la maniere du delta encoding"""
    assert type(tab) == list and tab != [], "tab doit etre un tableau non vide"
    resultat = [tab[0]]
    for i in range(1, len(tab)):  # on commence a l'indice 1
        # on calcule la difference entre l'actuel et le precedent
        diff = tab[i] - tab[i - 1]
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
        """Renvoie True si et seulement si le noeud est une feuille"""
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = ""  # on initialise l'expression
    if e.gauche is not None:
        s = s + expression_infixe(e.gauche)  # on ajoute l'expression du SAG
    s = s + str(e)  # on ajoute la valeur de la racine
    if e.droit is not None:
        s = s + expression_infixe(e.droit)  # on ajoute l'expression du SAD
    if e.est_une_feuille():  # si e est une feuille, on retourne juste l'expression
        return s
    return "(" + s + ")"
