def fusion(tab1: list, tab2: list) -> list:
    """renvoie un tableau etant la fusion de tab1 et tab2"""
    assert type(tab1) == type(tab2) == list, "tab1 et tab2 doivent etre des tableaux"
    assert tab1 != [] and tab2 != [], "tab1 et tab2 doivent etre non vides"
    tab = []
    n1, n2 = len(tab1), len(tab2)
    i1, i2 = 0, 0
    while i1 < n1 and i2 < n2:  # tant que i1 < n1 et i2 < n2
        if tab1[i1] < tab2[i2]:
            tab.append(tab1[i1])
            i1 += 1
        else:
            tab.append(tab2[i2])
            i2 += 1
    while i1 < n1:
        tab.append(tab1[i1])
        i1 += 1
    while i2 < n2:
        tab.append(tab2[i2])
        i2 += 1
    return tab


def rom_to_dec(nombre):
    """Renvoie l’écriture décimale du nombre donné en chiffres romains"""
    # on complete le dico
    dico = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if len(nombre) == 1:
        return dico[nombre]  # s'il n'y qu'un nombre on renvoie sa valeur

    else:
        ### on supprime le premier caractère de la chaîne contenue dans la variable nombre
        ### et cette nouvelle chaîne est enregistrée dans la variable nombre_droite
        nombre_droite = nombre[1:]

        if dico[nombre[0]] >= dico[nombre[1]]:  # on renvoie la valeur + la droite
            return dico[nombre[0]] + rom_to_dec(nombre_droite)
        else:  # on renvoie la droite - la valeur
            return rom_to_dec(nombre_droite) - dico[nombre[0]]


assert rom_to_dec("CXLII") == 142
