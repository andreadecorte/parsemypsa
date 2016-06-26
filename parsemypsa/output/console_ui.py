#!/usr/bin/env python

import logging

from prompt_toolkit import prompt

from parsemypsa.output import computation


def menu_actions():
    """Encapsulate the actions to execute for lazy evaluation"""
    # Maps an int to its message and the connected method (except for exit)
    actions = {
        0: ("exit", "bye"),
        1: ("vehicle information", computation.display_basic_info()),
        2: ("average consumption", computation.compute_mileage()),
        3: ("average consumption (km/l)", computation.compute_mileage_kml()),
        4: ("last trip info", computation.display_last_trip()),
        5: ("average trip info", computation.display_average_trip_info()),
        6: ("trip list", computation.display_trip_list())
    }
    return actions


def display(one_shot=False):
    """:param one_shot True if we want to use just 1 answer, not an infinite loop (for tests)"""
    answer = 1
    # variable to avoid a continuous loop whuich makes hard unit tests
    passed = False
    while answer != 0 and not (one_shot and passed):
        try:
            raw_answer = input(return_menu())
            answer = int(raw_answer)

            print("%s:\n%s" % (menu_actions()[answer][0], menu_actions()[answer][1]))
        except (ValueError, KeyError):
            logging.warning("Invalid choice %s" % raw_answer)
        finally:
            passed = True


def return_menu():
    return "\n".join("%i for %s" % (key, val[0]) for key, val in menu_actions().items()) + "\n"
