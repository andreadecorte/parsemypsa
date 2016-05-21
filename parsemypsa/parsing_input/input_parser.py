#!/usr/bin/env python

from storage import objects


def parse_input_file(input_file):
    vin = input_file["vin"]
    print("Working on %s\n" % vin)

    trips = []
    for the_trip in input_file["trips"]:
        trips.append(objects.Trip.create(id=the_trip["id"], timestamp=the_trip["dte"], duration=the_trip["tme"], distance=the_trip["dst"], fuel_consumation=the_trip["vol"], typ=the_trip["typ"], merged=the_trip["mgd"]))

    vi = input_file["vehicleinformation"]
    alerts = parse_alerts(vin=vin, vehicle_information=vi)
    info = objects.VehiculeInformation.create(vin=vin, updatedon=vi["updatedon"], mileage=vi["mileage"], endlatitude=vi["endlatitude"], endlongitude=vi["endlongitude"], destlatitude=vi["destlatitude"],
                               destlongitude=vi["destlongitude"], distancetonextmaintenance=vi["distancetonextmaintenance"], daysuntilnextmaintenance=vi["daysuntilnextmaintenance"], maintenancepassed=vi["maintenancepassed"],
                                              fuellevel=vi["fuellevel"], fuelautonomy=vi["fuelautonomy"], endpositionaddrtext=vi["endpositionaddrtext"], destinationpositionaddrtext=vi["destinationpositionaddrtext"])

    return vin, trips, info


def parse_alerts(vin, vehicle_information):
    alerts = []
    for the_alert in vehicle_information["alerts"]:
        alerts.append(objects.Alert.create(vin=vin, id=the_alert["id"], date=the_alert["date"], issolved=the_alert["issolved"]))
    return alerts
