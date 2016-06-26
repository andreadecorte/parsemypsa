#!/usr/bin/env python

import unittest
from playhouse.test_utils import test_database
from peewee import *

from parsemypsa.storage import objects
from parsemypsa.output import computation

# Data for testing
test_db = SqliteDatabase(':memory:')
model_list = [objects.Alert, objects.VehiculeInformation, objects.Trip]


class OutputComputationTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def prepare_db(self):
        self.trip1 = objects.Trip.create(id=1, timestamp=1462731168, duration=200, distance=10000, fuel_consumation=1, typ=0, merged=0)
        self.trip2 = objects.Trip.create(id=2, timestamp=1462731168, duration=400, distance=7500, fuel_consumation=1, typ=0, merged=0)
        self.vin1 = objects.VehiculeInformation.create(vin="A6789BHN", updatedon=1465420687, mileage=37150, endlatitude=0, endlongitude=0, destlatitude=-1, destlongitude=-1, distancetonextmaintenance=19200, daysuntilnextmaintenance=65535, maintenancepassed=0, fuellevel=35, fuelautonomy=310, endpositionaddrtext="", destinationpositionaddrtext="")

    def test_mileage_calculation(self):
        with test_database(test_db, model_list):
            self.prepare_db()
            self.assertEqual(computation.compute_mileage(), 11.667)

    def test_mileage_kml_calculation(self):
        with test_database(test_db, model_list):
            self.prepare_db()
            self.assertEqual(computation.compute_mileage_kml(), 8.75)

    def test_mileage_calculation_empty_db(self):
        with test_database(test_db, model_list):
            self.assertEqual(computation.compute_mileage(), 0.0)

    def test_mileage_calculation_kml_empty_db(self):
        with test_database(test_db, model_list):
            self.assertEqual(computation.compute_mileage_kml(), 0.0)

    def test_average_trip_duration(self):
        with test_database(test_db, model_list):
            self.prepare_db()
            self.assertEqual(computation.compute_average_trip_duration(), 300.0)

    def test_average_trip_duration_empty_db(self):
        with test_database(test_db, model_list):
            self.assertEqual(computation.compute_average_trip_duration(), 0.0)

    def test_average_trip_length(self):
        with test_database(test_db, model_list):
            self.prepare_db()
            self.assertEqual(computation.compute_average_trip_length(), 8750.0)

    def test_average_trip_length_empty_db(self):
        with test_database(test_db, model_list):
            self.assertEqual(computation.compute_average_trip_length(), 0.0)

    def test_average_trip_info(self):
        with test_database(test_db, model_list):
            self.prepare_db()
            self.assertEqual(computation.display_average_trip_info(), "Length: 8750.0 Duration: 300.0")

    def test_display_basic_info(self):
        with test_database(test_db, model_list):
            self.prepare_db()
            self.assertEqual(computation.display_basic_info(), "Info about vehicle A6789BHN: Mileage: 37150 Autonomy: 310 Fuel level: 35.0 Next manteinance in 19200 km")

    def test_display_basic_info_empty_db(self):
        with test_database(test_db, model_list):
            self.assertEqual(computation.display_basic_info(), "")

    def test_last_trip_empty_db(self):
        with test_database(test_db, model_list):
            self.assertEqual(computation.display_last_trip(), "")

    def test_display_trip_list(self):
        with test_database(test_db, model_list):
            self.prepare_db()
            self.assertEqual(computation.display_trip_list(), "Trip 1 started on 1462731168, lasted 200 minutes and 10000 m\nTrip 2 started on 1462731168, lasted 400 minutes and 7500 m\n")

    def test_display_trip_list_empty_db(self):
        with test_database(test_db, model_list):
            self.assertEqual(computation.display_trip_list(), "")
