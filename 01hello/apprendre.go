package main

import (
	"fmt"
)

// TD SUR LES STRUCTURES REPETITIVES

/*func calculerFactorielle(n int) int {
	var fact int
	fact = 1
	if n == 0 {
		fact = 1
	}
	for i := 1; i <= n; i++ {

		fact = fact * i
	}

	return fact
}

func main() {
	var n int
	fmt.Print("entrez la valeur de n: ")
	fmt.Scan(&n)
	resultat := calculerFactorielle(n)
	fmt.Printf("la factorielle de %d est: %d\n", n, resultat)
}
*/

// 3.2 puissance
/*func calculerPuissance(x int, n int) int {
	var resultat int
	var i int
	resultat = 1
	if n == 0 {
		resultat = 1
	}

	for i = 1; i <= n; i++ {
		resultat = resultat * x

	}
	return int(resultat)
}

func main() {
	var (
		x int
		n int
	)
	fmt.Print("veuillez entrer le nombre x : ")
	fmt.Scan(&x)
	fmt.Print("veuillez entrer l'exposant n: ")
	fmt.Scan(&n)
	puissance := calculerPuissance(x, n)
	fmt.Printf("%d puissance %d donne : %d\n", x, n, puissance)
}
*/

// 3.3 table de multiplication
/*func faireMultiplication(n int) {
	for i := 0; i <= n+1; i++ {
		fmt.Printf("%d * %d = %d\n", i, n, n*i)
	}
}
func main() {
	var n int
	fmt.Print("entrez la valeur de n: ")
	fmt.Scan(&n)
	faireMultiplication(n)
	fmt.Printf("VOICI LA TABLE DE MULTIPLICATION DE %d\n ", n)
}
*/

// 3.5 affichage

/*func afficherLignesEnt(n int) {
	for i := 1; i <= n; i++ {
		for j := i; j >= 1; j-- {
			fmt.Print(j, " ")
		}
		fmt.Println()
	}
}

func main() {
	var n int
	fmt.Print("entrez le nombre : ")
	fmt.Scan(&n)
	afficherLignesEnt(n)
}*/

//3.6 Deviner

func devinerNombre(nombre int, n1 int) {
	var nbCoups int
	for {
		nbCoups++
		if nombre > n1 {
			fmt.Println("c'est trop grand!: ")
			fmt.Print("veuillez entrer un autre nombre: ")
			fmt.Scan(&nombre)

		} else if nombre < n1 {
			fmt.Print("c'est trop petit!: ")
			fmt.Print("veuillez entrer un autre nombre: ")
			fmt.Scan(&nombre)

		} else {

			fmt.Printf("Bravo ! vous avez gagné en %d coups\n", nbCoups)
			break
		}

	}
}

func main() {
	var n1 int
	var nombre int
	fmt.Println("premier joueur: ")

	fmt.Print("entrez un nombre aléatoire: ")
	fmt.Scan(&n1)

	fmt.Println("deuxième joueur: ")

	fmt.Print("veuillez entrez un nombre compris entre 0 et 100")
	fmt.Scan(&nombre)
	for nombre < 0 || nombre > 100 {
		fmt.Print("entrez un nombre compris dans l'intervalle!!!: ")
		fmt.Scan(&nombre)
	}
	devinerNombre(nombre, n1)
}
