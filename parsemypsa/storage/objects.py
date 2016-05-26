#!/usr/bin/env python

from peewee import *
import datetime

# Initialize without DB, will be specified at runtime
database = SqliteDatabase(None)


class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = database


class Trip(BaseModel):
    """Represents a Trip"""
    id = IntegerField(primary_key=True)
    timestamp = IntegerField()
    # Seconds?
    duration = IntegerField()
    # Meters
    distance = IntegerField()
    # liters
    fuel_consumation = FloatField()
    typ = IntegerField()
    merged = SmallIntegerField()

    # Calculated
    mileage = FloatField(null=True)
    mileage_kml = FloatField(null=True)

    def calculate_mileage(self):
        """l / 100 km"""
        self.mileage = self.fuel_consumation / ((self.distance / 1000) / 100)

    def calculate_mileage_kml(self):
        """km / l"""
        self.mileage_kml = (self.distance / 1000) / self.fuel_consumation

    def return_formatted_date(self):
        return datetime.datetime.fromtimestamp(int(self.timestamp)).strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return "Trip %s lasted %i" % (self.id, self.duration)


class VehiculeInformation(BaseModel):
    vin = CharField(primary_key=True)
    updatedon = IntegerField()
    mileage = IntegerField()
    endlatitude = DoubleField()
    endlongitude = DoubleField()
    destlatitude = DoubleField()
    destlongitude = DoubleField()
    distancetonextmaintenance = IntegerField()
    daysuntilnextmaintenance = IntegerField()
    maintenancepassed = IntegerField()
    fuellevel = FloatField()
    fuelautonomy = IntegerField()
    endpositionaddrtext = CharField()
    destinationpositionaddrtext = CharField()


class Alert(BaseModel):
    vin = ForeignKeyField(VehiculeInformation, related_name='alerts')
    id = SmallIntegerField(primary_key=True)
    date = IntegerField()
    is_solved = SmallIntegerField(null=True)


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
