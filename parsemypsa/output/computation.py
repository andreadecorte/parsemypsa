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
        # rounded to 3 decimals
        result = round(mileage / len(objects.Trip.select()), 3)
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
        # rounded to 3 decimals
        result = round(mileage_kml / len(objects.Trip.select()), 3)
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
        result = round(result, 3)
    except ZeroDivisionError:
        logging.warning("No trips in the DB!")

    logging.debug("Average trip duration: %f" % result)
    return result


def compute_average_trip_length():
    """Average length in meters for the trip"""
    result = 0.0
    for trip in objects.Trip.select():
        result = result + trip.distance

    try:
        result /= len(objects.Trip.select())
        result = round(result, 3)
    except ZeroDivisionError:
        logging.warning("No trips in the DB!")

    logging.debug("Average trip length (meters): %f" % result)
    return result


def display_basic_info():
    """Returns basic info on the vehicle"""
    result = ""
    try:
        info = objects.VehiculeInformation.select()[0]
        result = "Info about vehicle {}: Mileage: {} Autonomy: {} Fuel level: {} Next manteinance in {} km".format(info.vin, info.mileage, info.fuelautonomy, info.fuellevel, info.distancetonextmaintenance)
    except IndexError:
        logging.warning("Empty DB!")
    logging.debug(result)
    return result


def display_last_trip():
    """Returns summary on last registered trip"""
    result = ""
    try:
        # Order by id DESC, take the first one, timestamp could be used too
        result = objects.Trip.select().order_by(objects.Trip.id.desc())[0]
    except IndexError:
        logging.warning("Empty DB!")
    logging.debug(result)
    return result


def display_average_trip_info():
    return "Length: %s Duration: %s" % (compute_average_trip_length(), compute_average_trip_duration())


def display_trip_list():
    """Display the list of all the trips"""
    result = ""
    for trip in objects.Trip.select():
        result += "%s\n" % trip

    logging.debug("List of trips: %s" % result)
    return result
