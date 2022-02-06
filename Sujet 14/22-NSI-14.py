def correspond(mot: str, mot_a_trous: str) -> bool:
    """renvoie True si le mot a trou correspond au mot, False sinon"""
    assert type(mot) == type(mot_a_trous) == str, "les mots doivent etre des chaines"
    assert mot.isupper() and mot_a_trous.isupper(), "les mots doivent etre majuscules"
    n1, n2 = len(mot), len(mot_a_trous)
    if n1 != n2:  # test de la longueur
        return False
    else:  # test lettre par lettre
        for i in range(n1):
            if mot[i] != mot_a_trous[i] and mot_a_trous[i] != "*":
                return False
        return True


def est_cyclique(plan):
    """
    Prend en paramètre un dictionnaire `plan` correspondant
    à un plan d'envoi de messages entre `N` personnes A, B, C,
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon.
    """
    personne = "A"
    N = len(plan)  # taille du plan
    for i in range(N - 1):
        if plan[personne] == "A":  # si le successeur est A
            return False  # on a trouve un cycle, False
        else:
            personne = plan[personne]  # sinon on passe au suivant
    return True  # si on atteint la fin le plan est cyclique
