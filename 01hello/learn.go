package main

import (
	"fmt"
)

//exercice 1

//exercice Partie 1
/*1-ici , le programme  fait a exposant b
2 les donnees sont :
-a
-b
resultat = 1
cpteur = 1
3 calcul : resultat = resultat * a
5- traduction en go */

//Exercice 3.7 passage à la caisse

func calculerSomme() (float64, int, float64) {

	var somme float64
	var nbArticles int
	var max float64
	nbArticles = 7
	somme = 0
	for i := 1; i <= nbArticles; i++ {
		var prixArticles float64
		fmt.Printf("entrez le prix de l'article numero %d : ", i)
		fmt.Scan(&prixArticles)
		somme += prixArticles
		max = calculerMaximum(prixArticles, max)
	}
	return somme, nbArticles, max
}

func calculerPrixMoyen(nbArticles int, somme float64) float64 {

	return somme / float64(nbArticles)

}

func calculerMaximum(prixArticles, max float64) float64 {

	if prixArticles > max {
		return prixArticles
	} else {
		return max
	}

}

func main() {

	prixF, nbArticles, max := calculerSomme()
	fmt.Println("la somme des articles achetés est: ", prixF)
	moyenneF := calculerPrixMoyen(nbArticles, prixF)
	fmt.Printf("le prix Moyen des articles achetés est: %.2f\n", moyenneF)

	fmt.Printf("l'article le plus cher vaut: %.2f\n", max)
}
