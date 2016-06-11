#!/usr/bin/env python

from playhouse.test_utils import test_database
from peewee import *

from parsemypsa.storage import objects, setup

# Data for testing
db_file = ':memory:'
test_db = SqliteDatabase(db_file)
model_list = [objects.Alert, objects.VehiculeInformation, objects.Trip]


def test_create_tables():
    with test_database(test_db, model_list):
        objects.database.init(db_file)
        setup.create_tables()
        assert test_db.get_tables() == ['alert', 'trip', 'vehiculeinformation']
