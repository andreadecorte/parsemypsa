#!/usr/bin/env python

import logging

from prompt_toolkit import prompt

from parsemypsa.output import computation


def display():
    answer = 1
    while answer != 0:
        answer = int(prompt(return_menu()))

        if answer == 1:
            computation.compute_mileage()
        elif answer == 2:
            computation.compute_mileage_kml()
        else:
            logging.warning("Invalid choice %s" % answer)


def return_menu():
    return "\n\n0 to exit:\n1 to to display average consumption\n2 to display average consumption (km/l)\n"
