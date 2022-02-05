def nombre_de_mots(phrase: str) -> int:
    """renvoie le nombre de mots presents dans la phrase"""
    compte = 0
    # il y a autant de mots que d'espace (+ 1 si on a un point '.' a la fin)
    for caractere in phrase:
        if caractere == " " or caractere == ".":
            compte += 1
    return compte


class Noeud:
    """
    Classe implémentant un noeud d'arbre binaire
    disposant de 3 attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre gauche.
    - droit : le sous-arbre droit.
    """

    def __init__(self, v, g, d):
        self.valeur = v
        self.gauche = g
        self.droite = d


class ABR:
    """
    Classe implémentant une structure
    d'arbre binaire de recherche.
    """

    def __init__(self):
        """Crée un arbre binaire de recherche vide"""
        self.racine = None

    def est_vide(self):
        """Renvoie True si l'ABR est vide et False sinon."""
        return self.racine is None

    def parcours(self, tab=[]):
        """
            Renvoie la liste tab complétée avec tous les
        éléments de
        l'ABR triés par ordre croissant.
        """
        if self.est_vide():
            return tab
        else:
            self.racine.gauche.parcours(tab)  # on parcours le SAG
            tab.append(self.racine.valeur)  # on ajoute la valeur de la racine
            self.racine.droite.parcours(tab)  # puis on parcours le SAD
            return tab

    def insere(self, element):
        """Insère un élément dans l'arbre binaire de recherche."""
        if self.est_vide():
            self.racine = Noeud(element, ABR(), ABR())
        else:
            if element < self.racine.valeur:
                self.racine.gauche.insere(element)
            else:
                self.racine.droite.insere(element)

    def recherche(self, element):
        """
        Renvoie True si element est présent dans l'arbre
        binaire et False sinon.
        """
        if self.est_vide():
            return False  # l'element n'est pas present si l'abr est vide
        else:
            if element < self.racine.valeur:
                # on recherche dans le SAG si element < racine
                return self.racine.gauche.recherche(element)
            elif element > self.racine.valeur:
                # on recherche dans le SAD si element > racine
                return self.racine.droite.recherche(element)
            else:
                # on retourne True si on l'a trouve
                return True
