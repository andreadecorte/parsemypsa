#!/usr/bin/env python

import unittest
from playhouse.test_utils import test_database
from peewee import *

from parsemypsa.storage import objects

# Data for testing
test_db = SqliteDatabase(':memory:')
model_list = [objects.Alert, objects.VehiculeInformation, objects.Trip]


class TripTestCase(unittest.TestCase):
    def setUp(self):
        with test_database(test_db, model_list):
            self.trip1 = objects.Trip.create(id=1, timestamp=1462731168, duration=200, distance=10000, fuel_consumation=1, typ=0, merged=0)

    def test_mileage_calculation(self):
        with test_database(test_db, model_list):
            self.trip1.calculate_mileage()
            self.assertEqual(self.trip1.mileage, 10.0)

    def test_mileage_kml_calculation(self):
        with test_database(test_db, model_list):
            self.trip1.calculate_mileage_kml()
            self.assertEqual(self.trip1.mileage_kml, 10.0)

    def test_formatted_date(self):
        with test_database(test_db, model_list):
            self.assertEqual(self.trip1.return_formatted_date(), "2016-05-08 18:12:48")

    def test_to_string(self):
        with test_database(test_db, model_list):
            self.assertEqual(str(self.trip1), "Trip 1 started on 1462731168, lasted 200 minutes and 10000 m")
