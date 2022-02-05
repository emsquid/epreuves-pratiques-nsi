def verifie(tab: list) -> bool:
    """renvoie True si tab est trie dans l'ordre croissant, False sinon"""
    assert type(tab) == list and tab != [], "tab doit etre un tableau non vide"
    for i in range(1, len(tab)):
        if tab[i] < tab[i - 1]:
            return False
    return True


urne = [
    "Oreilles sales",
    "Oreilles sales",
    "Oreilles sales",
    "Extra Vomit",
    "Lady Baba",
    "Extra Vomit",
    "Lady Baba",
    "Extra Vomit",
    "Lady Baba",
    "Extra Vomit",
]


def depouille(urne):
    resultat = dict()  # initialisation d'un dictionnaire vide
    for bulletin in urne:
        if bulletin in resultat.keys():  # si on a deja enregistre on incremente
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1  # sinon on initialise a 1
    return resultat


def vainqueur(election):
    vainqueur = ""  # a quoi sert cette variable ?
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:  # si le candidat a + de voix que le max
            nmax = election[candidat]  # il devient le nouveau max
            vainqueur = candidat
    # on fait une liste avec tous les candidats ayant autant de voix que le max
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale  # et on la renvoie
