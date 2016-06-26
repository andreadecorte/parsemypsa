#!/usr/bin/env python

import sys

from playhouse.test_utils import test_database
from peewee import *

from parsemypsa import main
from parsemypsa.parsing_input import input_parser
from parsemypsa.storage import objects


# Data for testing
db_file = ':memory:'
test_db = SqliteDatabase(db_file)
model_list = [objects.Alert, objects.VehiculeInformation, objects.Trip]


def test_input_file():
    input_file = "tests/trips.test"
    # Clear args
    sys.argv.clear()
    # First is program name
    sys.argv.append("parseMyPSA")
    # Then positional arguments
    sys.argv.append(input_file)
    args = main.option_parser()
    assert args.input_file == input_file
    parsed_file = main.file_opener(args)
    with test_database(test_db, model_list):
        vin, trips, info = input_parser.parse_input_file(parsed_file)
        assert vin == "AA"
        assert objects.Trip.get(objects.Trip.id == 38).distance == 16500
        assert objects.Alert.get(objects.Alert.vin == "AA").id == 108
