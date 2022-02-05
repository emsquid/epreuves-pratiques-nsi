def calcul(n: int) -> list:
    """renvoie la suite de syracuse en partant de n"""
    assert type(n) == int and n > 0, "n est un entier strictement positif"
    suite = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n) + 1
        suite.append(n)
    return suite


dico = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


def est_parfait(mot):
    # mot est une chaîne de caractères (en lettres majuscules)
    assert mot.isupper(), "mot doit etre en majuscules"
    code_c = ""
    code_a = 0  # code additionne, initialise a 0
    for c in mot:
        code_c = code_c + str(dico[c])  # on ajoute la str du code de la lettre
        code_a = code_a + dico[c]  # on additionne le code de la lettre
    code_c = int(code_c)
    # si le code concatene est divisible par le code additionne
    if code_c % code_a == 0:
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return [code_a, code_c, mot_est_parfait]
