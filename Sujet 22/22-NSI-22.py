def renverse(mot: str) -> str:
    """renvoie le mot inverse"""
    assert type(mot) == str and mot != "", "mot est une chaine non vide"
    # solution facile : return mot[::-1]
    inverse = ""
    for lettre in mot:
        inverse = lettre + inverse
    return inverse


def crible(N):
    """renvoie un tableau contenant tous les nombres premiers plus petit que N"""
    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False
    for i in range(2, N):  # 0 et 1 ne sont pas premiers, on commence a 2
        if tab[i] == True:  # si i est premier
            premiers.append(i)  # on l'ajoute a la liste
            for multiple in range(2 * i, N, i):
                tab[multiple] = False  # puis on met a False ses multiples
    return premiers


assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
