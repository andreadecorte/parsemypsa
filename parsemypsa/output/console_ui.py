#!/usr/bin/env python

import logging

from prompt_toolkit import prompt

from storage import objects


def display():
    answer = 1
    while answer != 0:
        answer = int(prompt(return_menu()))

        if answer == 1:
            mileage = 0
            for trip in objects.Trip.select():
                trip.calculate_mileage()
                logging.debug("%f, %f, %f" % (trip.fuel_consumation, trip.distance, trip.mileage))
                mileage = mileage + trip.mileage

                logging.debug("Average consumption: %f" % ( mileage /len(objects.Trip.select())))
            print("Average consumption: %f" % ( mileage /len(objects.Trip.select())))
        elif answer == 2:
            mileage_kml = 0
            for trip in objects.Trip.select():
                trip.calculate_mileage_kml()
                logging.debug("%f, %f, %f" % (trip.fuel_consumation, trip.distance, trip.mileage_kml))
                mileage_kml = mileage_kml + trip.mileage_kml

            logging.debug("Average consumption (km/l): %f" % (mileage_kml /len(objects.Trip.select())))
            print("Average consumption (km/l): %f" % (mileage_kml / len(objects.Trip.select())))
        else:
            logging.warning("Invalid choice %s" % answer)


def return_menu():
    return "\n\n0 to exit:\n1 to to display average consumption\n2 to display average consumptio (km/l)\n"
