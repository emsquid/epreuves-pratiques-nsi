def fibonacci(n: int) -> int:
    """renvoie le n ieme nombre de la suite de fibonacci (prog dynamique)"""
    assert type(n) == int and n > 0, "n doit etre un entier strictement positif"
    tab_fib = [None] * (n + 1)  # on initialise un tableau de taille n + 1
    tab_fib[1], tab_fib[2] = 1, 1  # on initialise les valeurs de u1 et u2
    for i in range(3, n + 1):  # puis on construit le reste du tableau
        tab_fib[i] = tab_fib[i - 1] + tab_fib[i - 2]
    return tab_fib[n]


liste_eleves = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]


def meilleures_notes():
    note_maxi = 0
    nb_eleves_note_maxi = 0
    liste_maxi = []

    for compteur in range(len(liste_notes)):
        if liste_notes[compteur] == note_maxi:  # si la note est la note maxi
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(liste_eleves[compteur])  # on ajoute l'eleve
        if liste_notes[compteur] > note_maxi:  # si la note est superieur a la note maxi
            note_maxi = liste_notes[compteur]  # on change la note maxi
            nb_eleves_note_maxi = 1  # on reinitialise le nb d'eleves a 1
            liste_maxi = [liste_eleves[compteur]]  # et la liste a l'eleve

    return (note_maxi, nb_eleves_note_maxi, liste_maxi)
