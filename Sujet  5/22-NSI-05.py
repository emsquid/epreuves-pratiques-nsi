def rechercheMinMax(tableau: list) -> dict:
    """renvoie la plus petite et la plus grande valeur du tableau
    sous la forme d'un dico"""
    if tableau == []:  # si le tableau est vide on renvoie des Nones
        return {"min": None, "max": None}
    else:  # sinon on initialise le min et le max au premier entier
        resultat = {"min": tableau[0], "max": tableau[0]}
        for entier in tableau:  # on itere sur les entiers
            if entier < resultat["min"]:  # on compare au min
                resultat["min"] = entier
            elif entier > resultat["max"]:  # puis au max sinon
                resultat["max"] = entier
        return resultat


class Carte:
    def __init__(self, c, v):
        """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
        assert 1 <= c <= 4, "la couleur doit etre entre 1 et 4"
        assert 1 <= v <= 13, "la valeur doit etre entre 1 et 13"
        self.Couleur = c
        self.Valeur = v

    def getNom(self):
        """Renvoie le nom de la Carte As, 2, ... 10,
        Valet, Dame, Roi"""
        if self.Valeur > 1 and self.Valeur < 11:
            return str(self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    def getCouleur(self):
        """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
        return ["pique", "coeur", "carreau", "trefle"][self.Couleur - 1]


class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    def remplir(self):
        """Remplit le paquet de cartes"""
        for c in range(1, 5):  # toutes les couleurs (entre 1 et 4)
            for v in range(1, 14):  # toutes les valeurs (entre 1 et 13)
                self.contenu.append(Carte(c, v))

    def getCarteAt(self, pos):
        """Renvoie la Carte qui se trouve à la position donnée"""
        assert (
            type(pos) == int and 0 <= pos < 51
        ), "le paquet contient 52 cartes, pos est un entier entre 0 et 51"
        # eventuellement (pos - 1) selon l'interpretation
        return self.contenu[pos]
