#!/usr/bin/env python

from peewee import *
from storage import objects

sqlite_db = SqliteDatabase('my_app.db')

def create_tables():
    sqlite_db.connect()
    sqlite_db.create_tables([objects.Alert, objects.VehiculeInformation, objects.Trip], True)