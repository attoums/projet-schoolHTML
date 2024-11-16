package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Agenda_temps struct {
	heure   int
	minute  int
	seconde int
}

type Agenda_evenement struct {
	nomEvenement string
	lieuEvent    string
	heureDebut   int
	heureFin     int
}
type Agenda struct {
	nomEvenement string
}

func input(message string) string {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print(message)
	scanner.Scan()
	return strings.TrimSpace(scanner.Text())
}

func saisirEvenement() Agenda_evenement {
	var evenementInput Agenda_evenement
	fmt.Println("VEUILLEZ SAISIR UN EVENEMENT ICI: ")

	evenementInput.nomEvenement = input("Nom du cours: ")

	evenementInput.lieuEvent = input("où se tiendra le cours ?: ")

	heureDebut := input("debut du cours : ")
	evenementInput.heureDebut, _ = strconv.Atoi(heureDebut)

	heureFin := input("fin du cours: ")
	evenementInput.heureFin, _ = strconv.Atoi(heureFin)

	return evenementInput

}

func afficherInformations(evenementInput Agenda_evenement) string {
	var informations string

	informations = fmt.Sprintf("cours:%s\n ,lieu :%s\n ,debut :%02dh%02d\n,fin:%02dh%02d\n", evenementInput.nomEvenement, evenementInput.lieuEvent, evenementInput.heureDebut, evenementInput.heureFin)
	return informations
}

func main() {
	agenda := []Agenda_temps{
		{17, 35, 28},
		{16, 25, 00},
	}
	for _, temps := range agenda {

		resultat := fmt.Sprintf("%02d:%02d:%02d", temps.heure, temps.minute, temps.seconde)
		fmt.Println(resultat)
	}
	var event []Agenda_evenement
	var n int
	fmt.Print("combien d'évenements souhaitez vous entrer? : ")
	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		evenements := saisirEvenement()
		event = append(event, evenements)
	}
	for _, event := range event {
		fmt.Println(afficherInformations(event))
	}

}
