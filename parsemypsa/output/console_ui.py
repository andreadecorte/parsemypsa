#!/usr/bin/env python

import logging

from prompt_toolkit import prompt

from parsemypsa.output import computation

menu_actions = {
    0: "exit",
    1: "display vehicle information",
    2: "display average consumption",
    3: "display average consumption (km/l)"
}


def display():
    answer = 1
    while answer != 0:
        try:
            raw_answer = prompt(return_menu())
            answer = int(raw_answer)

            if answer == 1:
                print("%s" % computation.display_basic_info())
            elif answer == 2:
                    print("Average consumption: %f" % computation.compute_mileage())
            elif answer == 3:
                print("Average consumption (km/l): %f" % computation.compute_mileage_kml())
            else:
                # Don't log an error if you want to exit
                if answer != 0:
                    logging.warning("Invalid choice %i" % answer)
        except ValueError:
            logging.warning("Invalid choice %s" % raw_answer)


def return_menu():
    return "\n".join("%i to %s" % (key, val) for key, val in menu_actions.items()) + "\n"
