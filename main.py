"""
Module pour exercices sur les tuples
"""

#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(1032) #permet de modifier la limite des appels qui est par défaut de 1000

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)"""

    # votre code ici
    carac = []
    occ = []
    carac.append(s[0])
    occ.append(1)
    indice = 0
    taille = len(s)
    for i in range(1, taille) :
        if s[i] == s[i-1] :
            occ[indice] += 1
        else :
            carac.append(s[i])
            occ.append(1)
            indice += 1
    liste = list(zip(carac, occ))

    return liste

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)"""

    # votre code ici

    if len(s) == 0 :
        return [] # cas de base

    # recherche nombre de caractères identiques au premier
    nb = 1
    for i in range(1, len(s)) :
        if s[i] == s[i-1] :
            nb += 1
        else :
            break
    return [(s[nb-1], nb)] + artcode_r(s[nb:]) # appel récursif

#### Fonction principale

def main():
    """
    fonction principale pour appeler les fonctions secondaires"""

    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
