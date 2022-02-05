def moyenne(tab: list) -> float:  # similaire au sujet 12
    """renvoie la moyenne du tableau"""
    assert type(tab) == list and tab != [], "tab doit etre un tableau non vide"
    # solution facile : return sum(tab) / len(tab)
    total = 0
    for element in tab:
        total += element
    return total / len(tab)


def dec_to_bin(a):  # identique au sujet 15
    bin_a = str(a % 2)
    a = a // 2
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a
