#!/usr/bin/env python

import vehiculeinformation
import trip


def parse_input_file(input_file):
    vin = input_file["vin"]
    print("Working on %s\n" % vin)

    trips = []
    for the_trip in input_file["trips"]:
        trips.append(trip.Trip(the_trip["id"], the_trip["dte"], the_trip["tme"], the_trip["dst"], the_trip["vol"], the_trip["typ"], the_trip["mgd"]))

    vi = input_file["vehicleinformation"]
    alerts = parse_alerts(vi)
    info = vehiculeinformation.VehiculeInformation(vi["updatedon"], vi["mileage"], vi["endlatitude"], vi["endlongitude"], vi["destlatitude"],
                               vi["destlongitude"], vi["distancetonextmaintenance"], vi["daysuntilnextmaintenance"], vi["maintenancepassed"],
                               vi["fuellevel"], vi["fuelautonomy"], vi["endpositionaddrtext"], vi["destinationpositionaddrtext"], alerts)

    return vin, trips, info


def parse_alerts(vehicle_information):
    alerts = []
    for the_alert in vehicle_information["alerts"]:
        alerts.append(vehiculeinformation.Alert(the_alert["id"], the_alert["date"], the_alert["issolved"]))
    return alerts
