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


def display(one_shot=False):
    """:param one_shot True if we want to use just 1 answer, not an infinite loop (for tests)"""
    answer = 1
    # variable to avoid a continuous loop whuich makes hard unit tests
    passed = False
    while answer != 0 and not (one_shot and passed):
        try:
            raw_answer = input(return_menu())
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
        finally:
            passed = True


def return_menu():
    return "\n".join("%i to %s" % (key, val) for key, val in menu_actions.items()) + "\n"
