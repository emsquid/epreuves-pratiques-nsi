def rendu(somme_a_rendre: int) -> list:
    """retourne 3 entiers correspondants aux nombre de billets/pieces a rendre"""
    assert (
        type(somme_a_rendre) == int and somme_a_rendre > 0
    ), "somme_a_rendre doit etre un entier positif non nul"
    n1 = somme_a_rendre // 5
    n2 = (somme_a_rendre % 5) // 2
    n3 = (somme_a_rendre % 5) % 2
    return [n1, n2, n3]


class Maillon:
    def __init__(self, v):
        self.valeur = v
        self.suivant = None


class File:
    def __init__(self):
        self.dernier_file = None

    def enfile(self, element):
        nouveau_maillon = Maillon(element)  # on cree un maillon
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon  # puis on l'associe a l'attribut dernier

    def est_vide(self):
        return self.dernier_file == None

    def affiche(self):
        maillon = self.dernier_file
        while maillon != None:
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self):
        if not self.est_vide():
            if self.dernier_file.suivant == None:  # on verifie si on a un seul element
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file  # on part du dernier
            while (
                maillon.suivant.suivant != None
            ):  # on itere jusqu'a trouver l'avant premier element
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur  # le resultat est la valeur du premier
            maillon.suivant = None  # on supprime le premier
            return resultat
        return None
