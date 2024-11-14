#générateur de mot de passe
import random

#demander à l'utilisateur de saisir la longueur du mot de passe 
longueur_mdp = int(input("donnez la longueur du mot de passe: "))
#liste des lettres majuscules , minicules et ponctuations
s ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&*_"
#selectionner aléatoirement les caractères et les joindre avec "join"
password = "".join(random.sample(s,longueur_mdp))
print(password)
