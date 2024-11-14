#EXERCICE 1 
"""
def calculerHeures(secondeInput):
    jours = secondeInput //86400
    reste_jour = secondeInput %86400

    heures = reste_jour //3600
    reste_heures = reste_jour %3600
    
    minutes = reste_heures //60
    reste_minutes = reste_heures %60

    secondes = reste_minutes
    return jours , heures , minutes,secondes


def main():
    secondeInput = int(input("entrez un entier(en secondes): "))
    jours , heures, minutes , secondes = calculerHeures(secondeInput)
    print(f"cela donne {jours} jours,{heures} heures,{minutes} minutes, {secondes} secondes")

main()    
    """
   
#EXERCICE 2
#1:
"""
def main():
    for n in range(10,0,-1):
        if n%2 == 0:
            print(n)

main()  
"""

#2
"""
def main():
    n = 10
    while n!=0:
        if n%2 !=0:
            print(n)
        n = n - 1

main()
"""

#3
"""
on doit privilégier le for car on connait le nombre d'itérations à l'avance
"""

#EXERCICE 3 
#1ere figure 
def afficherFigure(n):
    for i in range(1,n+1):
        for j in range(1, n+1):
            print("*",end = "")
        print()


#2e figure
def afficherFigure2(n):
    for i in range (n,0,-1):
        print("*"*i)           

#3e figure
def  afficherFigure3(n):
    for i in range(n):
        print(" "*i, "*"*n)
        n = n-1


#4e figure
def afficherFigure4(n):


    for i in range(n):
        for j in range(n):
            if (
                (i == 0)  or 
                (i == n-1) 
                
            ):
                print("*", end = " ")
            else:    
                print(end = " ")  



def main():
  
    afficherFigure4(5)

main()                  