"""
  
    
#version normale
def tri_bulles(tab):
    taille = len(tab)
    for i in range(taille-1,-1,-1):
        for j in range(i):
            if tab[j+1] < tab[j]:
                perm = tab[j+1]
                tab[j+1] = tab[j]
                tab[j] = perm

    return tab
    
    """
""" 

#version optimisée
def tri_bulles(tab):
    taille = len(tab)
    for i in range(taille-1,-1,-1):
        est_trie = True
        for j in range(i):
            if tab[j+1] < tab[j]:
                perm = tab[j+1]
                tab[j+1] = tab[j]
                tab[j] = perm
                est_trie = False
        if est_trie:
            return tab 

    return tab            

"""

""" 
def tri_par_insertion(l):
    for i in range(1,len(l)):
        cle = l[i]
        j= i-1
        while (j>=0 and cle < l[j]):
            l[j],l[j+1] = l[j+1], l[j]
            j-= 1

"""

"""def inverser_Tableau(tab):
    longueur = len(tab)
    for i in range(len(tab)//2):
        tab[i],tab[longueur-1-i] = tab[longueur-1-i],tab[i]

    return tab


def main():
    tab =[5,4,3,2,1,0]
    print(inverser_Tableau(tab))

main()    
"""

def tri_par_fusion(liste1, liste2):
    i1 = 0
    i2 = 0
    liste_total = []

    while i1 != len(liste1) and i2 != len(liste2):
        if liste1[i1] < liste2[i2]:
            liste_total.append(liste1[i1])
            i1 += 1
        else:
            liste_total.append(liste2[i2])
            i2 += 1

    return liste_total + liste1[i1:] + liste2[i2:]

def decomposition(liste):
    # Cas de base : si la liste est de taille 1 ou vide, elle est déjà triée
    if len(liste) <= 1:
        return liste

    # Diviser la liste en deux parties
    milieu = len(liste) // 2
    gauche = liste[:milieu]  # Première moitié
    droite = liste[milieu:]   # Seconde moitié

    # Appliquer récursivement le tri sur les deux moitiés
    gauche_triee = decomposition(gauche)
    droite_triee = decomposition(droite)

    # Fusionner les deux sous-listes triées
    return tri_par_fusion(gauche_triee, droite_triee)


def main():
    liste = [8,9,7,1,3,5]
    print(decomposition(liste))

main()    
