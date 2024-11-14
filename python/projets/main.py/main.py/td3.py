"""F0NCTIONS SIMPLES SUR LES LISTES"""
#EXERCICE 1

def create_liste():
    #initialisation de la liste 
    liste = []
    #initialisation de la variable booléene pour stopper
    listelt = True
    #tant qu'il ne met pas "stop"
    while listelt != "stop": 
        
        #on demande à l'utilisateur d'entrer des elements 
        listelt = input("entrez des elements de la liste: ")
        #on ajoute ces elements dans la liste avec 'append'
        liste.append(listelt)
    #si celui-ci entre stop , alors on sort de la boucle et on retourne la liste
    return list(liste)   
          
       


def main():
    resultat = create_liste()
    print(f"voici votre liste: {resultat} ")

main()    

"""
#EXERCICE 2

def take(n , liste_entier):
        #créer une nouvelle liste pour stocker les n premiers
        npremiers = []
        #pour i allant de 0 à n
        for i in range(n):
                 #ajouter à npremiers les n premiers element de liste_entier
                 npremiers.append(liste_entier[i])
        #retourner la valeur de "npremiers"
        return npremiers   
#EXERCICE 3 
def drop(n,liste_entier):
      nprive = []
     
      for i in range(n,len(liste_entier)):
              nprive.append(liste_entier[i])
           
      return liste_entier            
              




def main2():
        liste_entier = [10,3,6,40,60]
        resultat = take(3,liste_entier)
        
        print(f"les n premiers élements de liste entier sont: {resultat}")
        resultat2 = drop(3,liste_entier)
        print(f"liste_entier privée de ses n premiers élements: {resultat2}")


main2()

"""
    








#EXERCICE 4 

def somme(liste):
    #initialiser la somme à 0
    somme = 0
    #pour chaque élement de la liste faire :
    for elt in liste :
        #on affecte somme à somme + element 
        somme = somme + elt
    return somme 

def main3():
    liste = [10,11,12,13,14,15]
    sommeTotal = somme(liste)
    print(f"la somme des élements de la liste est: {sommeTotal}")

main3()    


#EXERCICE 5
def pairs_impairs(liste_entier):
        pairs = []
        impairs = []
        for n in range(len(liste_entier)):
                if n %2 == 0:
                        pairs.append(n)
                else:
                        impairs.append(n)        
        return pairs , impairs  

def main4():
        liste_entier = [4,5,6,8,2,3,9,47]
        p, imp = pairs_impairs(liste_entier)
        print(f"la liste des nombres pairs: {p}, et des impairs {imp}")

main4()        



#EXERCICE 6
def split_at(n,liste):
        div1 = liste[:len(liste)//n]

        div2 = liste[len(liste)//n: ]

        return div1 , div2

def main5():
        liste = [4,5,8,3,45,7,12,3,5]
        print(split_at(2,liste))

main5()        



#EXERCICE 7 

def to_str(liste):
        "initialisation de char"
        char = ""
        #pour chaque element dans la liste 
        for elt in liste:
                #on ajoutet à char la version string de elt et on ajoute une virgule 
                char += str(elt) + ","
       #on retourne len(char)-1 pour ne pas avoir de virgules à la fin 
        return char[0:len(char)-1]

def main6():
        liste = [1,2,3,4]
        resultat = to_str(liste)
        print(resultat)
main6()

"""2 COMPTEUR DE MOTS"""     

def compter_mots(phrase):
        somme = 0
       
        if phrase == "":
                somme = 0
                print("aucun mot")
        else:
                mots= phrase.split()
                somme = len(mots)

        return somme         



        



def main7():
        
        phrase = input("entrez une phrase: ")  
        resultat = compter_mots(phrase)      
        print(f"il y'a {resultat} mots dans cette phrase")
       
main7()       



