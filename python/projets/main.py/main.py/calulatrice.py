import tkinter as tk


calcul = ""

def afficher_touche_calcul(symbole):
    global calcul
    calcul += str(symbole)
    text_resultat.delete(1.0,"end")
    text_resultat.insert(1.0,calcul)

def evaluation_calcul():
    global calcul
    try:
        calcul = str(eval(calcul))
        #supprimer l'element de la 1ere ligne jusqu'a la fin
        text_resultat.delete(1.0,"end")
        #insérer le nouveau calcul à la 1ere ligne
        text_resultat.insert(1.0,calcul)

    except:
        effacer_ecran
        text_resultat.insert(1.0,"erreur!")

def effacer_ecran():
    #spécifier que calcul sera utilisé dans tout le programme
    global calcul
    #initialiser calcul à un string vide ""
    calcul = ""
    text_resultat.delete(1.0,"end")


interface = tk.Tk()
interface.geometry("300x275")   
interface.title("calculatrice de emmanuel") 



text_resultat = tk.Text(interface,height=2,width=16,font=('Arial',24))

text_resultat.grid(columnspan= 5)

#configuration des touches...
touche1 = tk.Button(interface,text ="1",command = lambda: afficher_touche_calcul(1),width = 5 ,font=('Arial',14) )
touche1.grid(row = 2 ,column= 1)

touche2 = tk.Button(interface,text ="2",command = lambda: afficher_touche_calcul(2),width = 5 ,font=('Arial',14) )
touche2.grid(row = 2 ,column= 2)

touche3 = tk.Button(interface,text ="3",command = lambda: afficher_touche_calcul(3),width = 5 ,font=('Arial',14) )
touche3.grid(row = 2 ,column= 3)

touche4 = tk.Button(interface,text ="4",command = lambda: afficher_touche_calcul(4),width = 5 ,font=('Arial',14) )
touche4.grid(row = 3 ,column= 1)

touche5 = tk.Button(interface,text ="5",command = lambda: afficher_touche_calcul(5),width = 5 ,font=('Arial',14) )
touche5.grid(row = 3 ,column= 2)

touche6 = tk.Button(interface,text ="6",command = lambda: afficher_touche_calcul(6),width = 5 ,font=('Arial',14) )
touche6.grid(row = 3 ,column= 3)

touche7 = tk.Button(interface,text ="7",command = lambda: afficher_touche_calcul(7),width = 5 ,font=('Arial',14) )
touche7.grid(row = 4 ,column= 1)

touche8 = tk.Button(interface,text ="8",command = lambda: afficher_touche_calcul(8),width = 5 ,font=('Arial',14) )
touche8.grid(row = 4 ,column= 2)

touche9 = tk.Button(interface,text ="9",command = lambda: afficher_touche_calcul(9),width = 5 ,font=('Arial',14) )
touche9.grid(row = 4 ,column= 3)

touche0 = tk.Button(interface,text ="0",command = lambda: afficher_touche_calcul(0),width = 5 ,font=('Arial',14) )
touche0.grid(row = 5 ,column= 2)

toucheopenB = tk.Button(interface,text ="(",command = lambda: afficher_touche_calcul("("),width = 5 ,font=('Arial',14) )
toucheopenB.grid(row = 5 ,column= 1)

touchecloseB = tk.Button(interface,text =")",command = lambda: afficher_touche_calcul(")"),width = 5 ,font=('Arial',14) )
touchecloseB.grid(row = 5 ,column= 3)

#il reste donc les opérations
touche_addition = tk.Button(interface,text ="+",command = lambda: afficher_touche_calcul("+"),width = 5 ,font=('Arial',14) )
touche_addition.grid(row = 2 ,column= 5)

touche_soustraction = tk.Button(interface,text ="-",command = lambda: afficher_touche_calcul("-"),width = 5 ,font=('Arial',14) )
touche_soustraction.grid(row = 3 ,column= 5)

touche_multiplication = tk.Button(interface,text ="x",command = lambda: afficher_touche_calcul("*"),width = 5 ,font=('Arial',14) )
touche_multiplication.grid(row = 4 ,column= 5)

touche_division = tk.Button(interface,text ="/",command = lambda: afficher_touche_calcul("/"),width = 5 ,font=('Arial',14) )
touche_division.grid(row = 5 ,column= 5)


touche_modulo= tk.Button(interface,text ="%",command = lambda: afficher_touche_calcul("%"),width = 5 ,font=('Arial',14) )
touche_modulo.grid(row = 6 ,column= 5)

#et aussi "égal" et "effacer"

touche_egal = tk.Button(interface,text ="=",command = evaluation_calcul,width = 5 ,font=('Arial',14) )
touche_egal.grid(row = 6 ,column= 3,columnspan = 2)


touche_effacer = tk.Button(interface,text ="C",command = effacer_ecran,width = 5 ,font=('Arial',14) )
touche_effacer.grid(row = 6 ,column= 1,columnspan = 2)





interface.mainloop()