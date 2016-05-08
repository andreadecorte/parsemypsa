#!/usr/bin/env python


class VehiculeInformation:
    def __init__(self, updateon, mileage, endlatitude, endlongitude, destlatitude, destlongitude, distancetonextmaintenance, daysuntilnextmaintenance, maintenancepassed, fuellevel, fuelautonomy, endpositionaddrtext, destinationpositionaddrtext, alerts):
        self._updatedon = updateon
        self._mileage = mileage
        self._alerts = alerts


class Alert:
    def __init__(self, id, date, issolved):
        self._id = id
        self._date = date
        self._is_solved = issolved

alert_mapping = {
    10: "Front left door open",
    11: "Porte avant droite ouverte",
    12: "Porte arrière gauche ouverte",
    13: "Porte arrière droite ouverte",
    15: "Coffre ouvert",
    22: "Niveau carburant faible",
    39: "Batterie faible",
    107: "Risque de verglas",
    108: "Porte avant droite ouverte(à l'arrêt, moteur en marche)",
    109: "Porte avant gauche ouverte(à l'arrêt, moteur en marche)",
    110: "Porte arrière droite ouverte(à l'arrêt, moteur en marche)",
    111: "Porte arrière gauche ouverte(à l'arrêt, moteur en marche)",
    112: "Coffre ouvert(à l'arrêt, moteur en marche)",
    125: "Défaut système freinage automatique",
    141: "Défaut moteur: faites réparer le véhicule"
}
