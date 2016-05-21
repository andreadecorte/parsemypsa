#!/usr/bin/env python

import unittest

from parsemypsa.storage import objects


class TripTestCase(unittest.TestCase):
    def setUp(self):
        self.trip1 = objects.Trip.create(id=1, 1462731168, 200, 1000, 1, 0, 0)

    def test_mileage_calculation(self):
        self.trip1.calculate_mileage()
        self.assertEqual(self.trip1._mileage, 1000)

    def test_formatted_date(self):
        self.assertEqual(self.trip1.return_formatted_date(), "2016-05-08 20:12:48")

    def test_to_string(self):
        self.assertEqual(str(self.trip1), "Trip 1 lasted 200")