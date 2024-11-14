tasks = []

def ajouterTask():
    tache = input("veuillez entrer une tache à accomplir: ")
    tasks.append(tache)
    print(f"tache'{tache}' ajouté à la liste :)")


def listerTask():
    if not tasks:
        print("il n'ya pas de taches actuellement.")
    else:
        print("taches actuelles: ")    
        for index, task in enumerate(tasks):
            print(f" tache #{index+1}. {task}")


def supprimerTask():
    listerTask()
    try:
        tacheAsupprimer = int(input("numero de la tache à supprimer: "))
        if tacheAsupprimer >=0 and tacheAsupprimer < len(tasks):
            tasks.pop(tacheAsupprimer)
            print(f"la tache {tacheAsupprimer} a été supprimée...")

        else:
            print(f" la Tache #{tacheAsupprimer} n'a pas éte trouvée")    
           
    except:    
        print("entrée invalide! ")




if __name__ == "__main__":
#créer une boucle pour executer l'application
    print("BIENVENUE DANS LA TODOLIST APP!")
    while True:
        print("\n")
        print(f"""
              veuillez selectionner une de ces options
              ----------------------------------------
              1. ajouter une nouvelle tache
              2. supprimer une tache
              3. lister taches
              4.quitter
              ---------------------------------------- 
              """)
       
        choix = input("quel est votre choix?: ")    

        if choix == "1":
            ajouterTask()


        elif choix =="2":    
            supprimerTask()


        elif choix =="3":    
            listerTask()

        elif choix =="4":    
            break

        else: 
            print("entrée non valide!, veuillez réésayer.")
    
    print("Au revoir!")
