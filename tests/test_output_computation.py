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
        self.trip2 = objects.Trip.create(id=2, timestamp=1462731168, duration=400, distance=10000, fuel_consumation=1, typ=0, merged=0)

    def test_mileage_calculation(self):
        with test_database(test_db, model_list):
            self.prepare_db()
            self.assertEqual(computation.compute_mileage(), 10.0)

    def test_mileage_kml_calculation(self):
        with test_database(test_db, model_list):
            self.prepare_db()
            self.assertEqual(computation.compute_mileage_kml(), 10.0)

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
