package main

import (
	"fmt"
)

/*- definir une fonction qui va verifier que le nombre n est présent
dans le tableau t
-faire une boucle de sorte que à chaque fois qu'il y 'aura le nombre n dans t ,
nombreoccurence = nombreoccurence+1
-demander à l'utilisateur de saisir 50 entiers
-
*/
//afficher le nombre d'etudiants inscrits

type etudiant struct {
	numeroEtudiant int
	nomEtudiant    string
	prenomEtudiant string
	ageEtudiant    int
}
type etudiant_cours struct {
	numeroCours   int
	nomCours      string
	nbHeuresCours int
}

type participations struct {
	numeroEtudiant int
	numeroCours    int
	notes          []float64
}

func afficherNbEtudiants(etudiants []etudiant) int {
	valeurs := len(etudiants)
	return valeurs
}

func afficherNomCours(cours []etudiant_cours) {
	for _, elt := range cours {
		fmt.Printf("%s\n", elt.nomCours)
	}
}

func identifierEtudiant(idEtudiant int, etudiants []etudiant) bool {
	for _, elt := range etudiants {
		if elt.numeroEtudiant == idEtudiant {
			fmt.Println("voici vos informations: ")
			return true

		}
	}
	fmt.Println("cet etudiant n'existe pas !! ERREUR")
	return false
}

func afficherNoteEtudiant(etudiants []etudiant, participation []participations, idEtudiant int) {

	for _, elt := range etudiants {
		if elt.numeroEtudiant == idEtudiant {
			fmt.Printf("%s\n", elt.prenomEtudiant)
			for _, p := range participation {
				if p.numeroEtudiant == elt.numeroEtudiant {
					fmt.Printf("%2.f\n", p.notes)
				}
			}
		}
	}
}

func main() {
	etudiants := []etudiant{

		{22313481, "Blon", "Sadia Deamess Emmanuel", 18},
		{22325589, "Nameli", "Axel Giroua", 22},
		{20123648, "Bilango", "Patrick", 20},
	}
	cours := []etudiant_cours{
		{244, "statistique descriptive", 25},
		{175, "introduction aux programmes informatiques", 36},
		{94, "algèbre linéaire", 50},
	}
	note1 := []float64{17.5, 14, 12}
	notes1p2 := []float64{16, 20}
	notesNameli := []float64{14, 9, 18, 15}

	participation := []participations{
		{22313481, 175, note1},
		{22313481, 94, notes1p2},
		{22325589, 244, notesNameli},
	}
	var idEtudiant int
	fmt.Print("quel est votre numeroEtudiant: ")
	fmt.Scan(&idEtudiant)

	resultat := afficherNbEtudiants(etudiants)
	fmt.Println("le nombre d'etudiants dans la base est : ", resultat)

	fmt.Printf("nom des cours disponibles :")

	afficherNomCours(cours)
	identifierEtudiant(idEtudiant, etudiants)

	afficherNoteEtudiant(etudiants, participation, idEtudiant)

}
