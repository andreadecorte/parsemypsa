#!/usr/bin/env python

import unittest.mock
import pytest

from playhouse.test_utils import test_database
from peewee import *

from parsemypsa.storage import objects
from parsemypsa.output import console_ui

# Data for testing
test_db = SqliteDatabase(':memory:')
model_list = [objects.Alert, objects.VehiculeInformation, objects.Trip]


def prepare_db():
    trip1 = objects.Trip.create(id=1, timestamp=1462731168, duration=200, distance=10000, fuel_consumation=1,
                                     typ=0, merged=0)
    trip2 = objects.Trip.create(id=2, timestamp=1462731168, duration=400, distance=7500, fuel_consumation=1, typ=0,
                                     merged=0)
    vin1 = objects.VehiculeInformation.create(vin="A6789BHN", updatedon=1465420687, mileage=37150, endlatitude=0,
                                                   endlongitude=0, destlatitude=-1, destlongitude=-1,
                                                   distancetonextmaintenance=19200, daysuntilnextmaintenance=65535,
                                                   maintenancepassed=0, fuellevel=35, fuelautonomy=310,
                                                   endpositionaddrtext="", destinationpositionaddrtext="")


def test_display():
    with test_database(test_db, model_list):
        prepare_db()
        with unittest.mock.patch('builtins.input', return_value="0"):
            assert console_ui.display() == None


def test_display_1(capsys):
    with test_database(test_db, model_list):
        prepare_db()
        with unittest.mock.patch('builtins.input', return_value="1"):
            console_ui.display(one_shot=True)
            out, err = capsys.readouterr()
            assert out == "Info about vehicle A6789BHN: Mileage: 37150 Autonomy: 310 Fuel level: 35.0 Next manteinance in 19200 km\n"


def test_display_2(capsys):
    with test_database(test_db, model_list):
        prepare_db()
        with unittest.mock.patch('builtins.input', return_value="2"):
            console_ui.display(one_shot=True)
            out, err = capsys.readouterr()
            assert out == "Average consumption: 11.667000\n"


def test_display_3(capsys):
    with test_database(test_db, model_list):
        prepare_db()
        with unittest.mock.patch('builtins.input', return_value="3"):
            console_ui.display(one_shot=True)
            out, err = capsys.readouterr()
            assert out == "Average consumption (km/l): 8.750000\n"

def test_display_invalid_choice(capsys):
    with test_database(test_db, model_list):
        prepare_db()
        with unittest.mock.patch('builtins.input', return_value="AA"):
            console_ui.display(one_shot=True)
            out, err = capsys.readouterr()
            # Exception caught and logged
            assert out == ""
