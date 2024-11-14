def quicksort(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste.pop()

    petit = []
    grand = []

    for nombre in liste:
        if nombre < pivot:
            petit.append(nombre)
        else:
            grand.append(nombre)

    return quicksort(petit)+ [pivot]+ quicksort(grand)        


def main():
    liste = [7,1,10,9,8,2,5,4,3,6]
    resultat = quicksort(liste)
    print(f"le tri rapide de la liste donne: {resultat}")

if __name__ == "__main__":
    main()    