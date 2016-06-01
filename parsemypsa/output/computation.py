#!/usr/bin/env python

import logging

from parsemypsa.storage import objects


def compute_mileage():
    mileage = 0
    result = 0.0
    for trip in objects.Trip.select():
        trip.calculate_mileage()
        logging.debug("%f, %f, %f" % (trip.fuel_consumation, trip.distance, trip.mileage))
        mileage = mileage + trip.mileage

    try:
        result = mileage / len(objects.Trip.select())
    except ZeroDivisionError:
        logging.warning("No trips in the DB!")

    logging.debug("Average consumption: %f" % result)
    return result


def compute_mileage_kml():
    mileage_kml = 0
    result = 0.0
    for trip in objects.Trip.select():
        trip.calculate_mileage_kml()
        logging.debug("%f, %f, %f" % (trip.fuel_consumation, trip.distance, trip.mileage_kml))
        mileage_kml = mileage_kml + trip.mileage_kml

    try:
        result = mileage_kml / len(objects.Trip.select())
    except ZeroDivisionError:
        logging.warning("No trips in the DB!")

    logging.debug("Average consumption (km/l): %f" % result)
    return result


def compute_average_trip_duration():
    result = 0.0
    for trip in objects.Trip.select():
        result = result + trip.duration

    try:
        result /= len(objects.Trip.select())
    except ZeroDivisionError:
        logging.warning("No trips in the DB!")

    logging.debug("Average trip duration: %f" % result)
    return result
