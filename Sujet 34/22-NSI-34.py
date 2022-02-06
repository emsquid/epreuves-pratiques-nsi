def occurrence_max(chaine: str) -> str:
    """renvoie le caractere le plus frequent de la chaine"""
    # je n'ai pas suivi les recommandations de l'exercice
    # car leur methode revient a une utilisation de dictionnaire sans dictionnaire
    assert type(chaine) == str and chaine != "", "chaine doit ne pas etre vide"
    freq = {chr(ord("a") + i): 0 for i in range(26)}  # dico contenant les frequences
    maxi = chaine[0]  # variable pour tenir freq de la lettre la plus frequente
    for caractere in chaine:
        if caractere in freq.keys():
            freq[caractere] += 1
            if freq[caractere] > freq[maxi]:
                maxi = caractere
    return maxi


def nbLig(image):
    """renvoie le nombre de lignes de l'image"""
    return len(image)


def nbCol(image):
    """renvoie la largeur de l'image"""
    return len(image[0])


def negatif(image):
    """renvoie le negatif de l'image sous la forme
    d'une liste de listes"""
    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(len(image)):  # pourquoi ne pas utiliser nbLig ???
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]  # x_n + x_i = 255 -> x_n = 255 - x_i
    return L


def binaire(image, seuil):
    """renvoie une image binarisee de l'image sous la forme
    d'une liste de listes contenant des 0 si la valeur
    du pixel est strictement inferieure au seuil
    et 1 sinon"""
    # l'exemple de cette fonction semble etre faux et renvoyé l'inverse
    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(len(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil:
                L[i][j] = 0  # 0 si le pixel est strictement inferieur au seuil
            else:
                L[i][j] = 1  # 1 sinon
    return L
