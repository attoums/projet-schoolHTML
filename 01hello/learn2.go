package main

import (
	"fmt"
)

// TD SUR LES FONCTIONS
//4.1 : hello world !

func foncB(message string, nbmessages int) {
	for cpteur := 0; cpteur < nbmessages; cpteur++ {
		fmt.Println("hello world!")
	}

}
func foncC(nbmessages int) int {
	var renvoi int
	if nbmessages > 10 {
		renvoi = 1
	} else {
		renvoi = 0
	}
	return renvoi

}

func main() {
	var message string
	var resultat int
	var nbmessages int
	nbmessages = 14

	foncB(message, 14)
	resultat = foncC(nbmessages)
	fmt.Println("renvoi: ", resultat)
}
