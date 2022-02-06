def max_dico(dico: dict) -> tuple:
    """renvoie le maximum du dico et sa cle"""
    assert type(dico) == dict and dico != {}, "dico doit etre un dictionnaire non vide"
    # j'utilise la fonction max pour recuperer la cle du maximum
    cle_max = max(dico, key=lambda cle: dico[cle])
    return (cle_max, dico[cle_max])


class Pile:
    """Classe definissant une structure de pile."""

    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie le booleen True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'element v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'element place au sommet de la pile,
        si la pile n'est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != "+" and element != "*":  # si l'element n'est pas un operateur
            p.empiler(element)  # on l'empile
        else:
            if element == "+":  # si c'est un +
                resultat = p.depiler() + p.depiler()  # on additionne les deux derniers
            else:  # sinon c'est un *
                resultat = p.depiler() * p.depiler()  # on multiplie les deux derniers
            p.empiler(resultat)  # on empile le resultat
    return p.depiler()  # a la fin on renvoi le seul element restant
