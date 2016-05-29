#!/usr/bin/env python

import logging

from storage import objects


def compute_mileage():
    mileage = 0
    for trip in objects.Trip.select():
        trip.calculate_mileage()
        logging.debug("%f, %f, %f" % (trip.fuel_consumation, trip.distance, trip.mileage))
        mileage = mileage + trip.mileage

        logging.debug("Average consumption: %f" % (mileage / len(objects.Trip.select())))
    print("Average consumption: %f" % (mileage / len(objects.Trip.select())))


def compute_mileage_kml():
    mileage_kml = 0
    for trip in objects.Trip.select():
        trip.calculate_mileage_kml()
        logging.debug("%f, %f, %f" % (trip.fuel_consumation, trip.distance, trip.mileage_kml))
        mileage_kml = mileage_kml + trip.mileage_kml

    logging.debug("Average consumption (km/l): %f" % (mileage_kml / len(objects.Trip.select())))
    print("Average consumption (km/l): %f" % (mileage_kml / len(objects.Trip.select())))
