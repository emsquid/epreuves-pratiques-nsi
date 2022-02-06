def moyenne(notes: list) -> float:
    """renvoie la moyenne ponderee de la liste de notes"""
    assert type(notes) == list and notes != [], "notes doit etre un tableau non vide"
    note_totale = 0
    coeff_total = 0
    for note, coeff in notes:  # on separe directement le couple (note, coeff)
        note_totale += note * coeff
        coeff_total += coeff
    return note_totale / coeff_total


def pascal(n):
    C = [[1]]
    for k in range(1, n + 1):  # on veut aller jusqu'a l'etape n (donc n + 1)
        Ck = [1]  # chaque ligne commence par 1
        for i in range(1, k):
            # k - 1 : ligne d'avant| i - 1 : colonne d'avant| i : colonne actuel
            Ck.append(C[k - 1][i - 1] + C[k - 1][i])
        Ck.append(1)  # chaque ligne se termine par 1
        C.append(Ck)
    return C
