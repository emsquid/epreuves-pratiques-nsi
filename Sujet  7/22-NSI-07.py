def conv_bin(n:int)->tuple:
    """renvoie le binaire de n et le nombre de bits qui le composent"""
    binaire = []
    while n > 0:
        binaire.append(n % 2) # on le reste de la division par 2
        n //= 2 # puis on divise n par 2
    binaire.reverse() # on retourne
    return (binaire, len(binaire))


def tri_bulles(T):
    n = len(T)
    for i in range(n - 1, -1, -1): # on boucle de n - 1 a 0
        for j in range(i):
            if T[j] > T[j+1]: # on compare chaque element au suivant
                # si besoin on echange
                temp = T[j] 
                T[j] = T[j+1]
                T[j+1] = temp
    return T
