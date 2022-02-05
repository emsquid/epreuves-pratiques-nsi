def maxliste(tab: list) -> int:
    """renvoie le plus grand element du tableau"""
    assert type(tab) == list and tab != [], "tab est un tableau non vide"
    # solution facile : return max(tab)
    maxi = tab[0]
    for element in tab:
        if element > maxi:
            maxi = element
    return maxi


class Pile:
    """Classe definissant une pile"""

    def __init__(self, valeurs=[]):
        self.valeurs = valeurs

    def est_vide(self):
        """Renvoie True si la pile est vide, False sinon"""
        return self.valeurs == []

    def empiler(self, c):
        """Place l'element c au sommet de la pile"""
        self.valeurs.append(c)

    def depiler(self):
        """Supprime l'element place au sommet de la pile, a  condition qu'��elle soit non vide"""
        if self.est_vide() == False:
            self.valeurs.pop()


def parenthesage(ch):
    """Renvoie True si la chaine chaine est bien parenthesee et False sinon"""
    p = Pile()
    for c in ch:
        if c == "(":  # si on a une parenthese ouvrante
            p.empiler(c)  # on l'empile
        elif c == ")":  # si on a une parenthese fermante
            if p.est_vide():
                return False  # si p est vide, mal parenthesee
            else:
                p.depiler()  # sinon on depile
    return p.est_vide()


assert parenthesage("((()())(()))") == True
assert parenthesage("())(()") == False
assert parenthesage("(())(()") == False
