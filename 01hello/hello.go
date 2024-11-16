package main

import (
	"fmt"
)

type avions_vols struct {
	numeroVol    int
	heureDepart  int
	heureArrivee int
}

func main() {
	vols := []avions_vols{
		{6119, 1625, 1730},
		{6120, 1514, 2155},
		{6121, 418, 930},
	}
	for _, vol := range vols {
		if vol.heureDepart >= vol.heureArrivee || (vol.heureDepart < 0 || vol.heureDepart > 2359) || (vol.heureArrivee < 0 || vol.heureArrivee > 2359) {
			fmt.Print("les heures de départ et d'arrivee ne sont pas valides")
		} else {
			heureDepart := fmt.Sprintf("%02dh%02d", vol.heureDepart/100, vol.heureDepart%100)
			heureArrivee := fmt.Sprintf("%02dh%02d", vol.heureArrivee/100, vol.heureArrivee%100)

			fmt.Printf("le vol N:%d départ: %s, arrivée: %s\n", vol.numeroVol, heureDepart, heureArrivee)
		}
	}
}
