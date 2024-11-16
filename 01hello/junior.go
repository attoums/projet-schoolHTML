package main

import (
	"fmt"
)

func effectuerControle(chiffre []int) int {
	for i := range chiffre {

		if i%2 != 0 {

			chiffre[i] = chiffre[i] * 2
		}
		if chiffre[i] > 9 {
			chiffre[i] = chiffre[i] - 9
		}
	}

	somme := 0
	for _, elt := range chiffre {
		somme = somme + elt
	}
	return somme
}

func verifierCode(somme int) {
	if somme%10 == 0 {
		fmt.Println("le code est correct")
	} else {
		fmt.Println("le code est incorrect!")
	}
}

func main() {
	var chiffre []int

	for {
		var input int
		fmt.Print("veuillez entrer un chiffre quelconque: ")
		_, err := fmt.Scan(&input)
		if err != nil {
			break
		}
		chiffre = append(chiffre, input)
		somme := effectuerControle(chiffre)
		verifierCode(somme)
	}
}
 // fin du code 
