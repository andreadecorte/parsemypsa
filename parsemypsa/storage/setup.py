#!/usr/bin/env python

from storage import objects

import logging
from peewee import *

model_list = [objects.Alert, objects.VehiculeInformation, objects.Trip]


def create_tables(drop_table=True):
    """Create a database for our data structure"""
    objects.database.connect()
    # Drop table if existing before recreating
    # TODO expose an option (but normally you should always recreate the db unless you change externally)
    if drop_table:
        logging.debug("Dropping tables before recreation")
        objects.database.drop_tables(models=model_list, safe=True)
    objects.database.create_tables(models=model_list, safe=True)