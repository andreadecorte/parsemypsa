#!/usr/bin/env python

import datetime


class Trip:
    """Represents a Trip"""
    def __init__(self, id, dte, tme, dst, vol, typ, mgd):
        self._id = id
        self._timestamp = dte
        self._duration = tme
        # meters
        self._distance = dst
        # liters
        self._fuel_consumation = vol
        self._type = typ
        self._merged = mgd

        # calculated
        self._mileage = 0

    def calculate_mileage(self):
        self._mileage = self._distance / self._fuel_consumation
        
    def return_formatted_date(self):
        return datetime.datetime.fromtimestamp(int(self._timestamp)).strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return "Trip %s lasted %i" % (self._id, self._duration)