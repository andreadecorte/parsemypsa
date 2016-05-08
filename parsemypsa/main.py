#!/usr/bin/env python

from _version import __version__ as VERSION
import input_parser
from trip import Trip

import argparse
import json
import logging
import sys


def main():
    # http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
    # https://stormpath.com/blog/building-simple-cli-interfaces-in-python/
    
    parser = argparse.ArgumentParser(description='Parse files produced by LinkMyPeugeot App.')
    parser.add_argument('input_file', metavar='input_file', nargs='?', help='input file to parse')
    parser.add_argument('--log-level', dest='log_level', help='logging level (e.g. DEBUG)', default='INFO')
    parser.add_argument('--version', dest='version', action='store_true', help='show the version and exit')

    args = parser.parse_args()
    
    if args.version:
        print_version()

    # Configure logging level by parsing the input parameter
    numeric_level = getattr(logging, args.log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.log_level)
    logging.basicConfig(level=numeric_level)
    
    with open('../my_psa1539272400.trips') as f:
        input_file = json.load(f)

    vin, trips, info = input_parser.parse_input_file(input_file)
    logging.debug("Trips read: %i" % len(trips))

    
def print_version():
    """Print version and exits"""
    print(VERSION)
    sys.exit(0)


if __name__ == "__main__":
    main()
