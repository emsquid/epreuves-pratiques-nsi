def mini(releve: list, date: list) -> tuple:
    """renvoie la plus petite valeur relevee et l'annee correspondante"""
    assert (
        len(releve) == len(date) != 0
    ), "il doit y avoir autant de releves que de dates, et pas 0"
    i_min = 0
    for i in range(len(releve)):
        if releve[i] < releve[i_min]:
            i_min = i
    return (releve[i_min], date[i_min])


def inverse_chaine(chaine):
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat  # on ajoute le caractere devant
    return resultat


def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse  # on verifie si la chaine est identique a son inverse


def est_nbre_palindrome(nbre):
    chaine = str(nbre)  # on convertit le nombre en chaine
    return est_palindrome(chaine)
