#!/usr/bin/env python

from parsemypsa._version import __version__ as VERSION
from parsemypsa.parsing_input import input_parser
from parsemypsa.storage import objects, setup
from parsemypsa.output import console_ui

import argparse
import json
import logging
import sys


def main():
    try:
        args = option_parser()
        if args.version:
            print_version()

        setup_logging(args)
        logging.debug("Arguments: %s" % args)

        # Init database and create tables
        objects.database.init(args.db_file)
        setup.create_tables()

        # Open input file
        parsed_file = file_opener(args=args)
        # Parse data into objects
        vin, trips, info = input_parser.parse_input_file(parsed_file)
        logging.debug("Trips read: %i" % len(trips))
        # Show UI
        console_ui.display()
    except KeyboardInterrupt:
        logging.info("Exiting")
        sys.exit(1)


def file_opener(args):
    if not args.input_file:
        # TODO offer list of files in current folder
        logging.warning("You need to specify an input file!")
        sys.exit(2)
    with open(args.input_file) as f:
        parsed_file = json.load(f)
    return parsed_file


def option_parser():
    parser = argparse.ArgumentParser(description='Parse files produced by LinkMyPeugeot App.')
    parser.add_argument('input_file', metavar='input_file', nargs='?', help='input file to parse')
    parser.add_argument('--log-level', dest='log_level', help='logging level (e.g. DEBUG)', default='INFO')
    parser.add_argument('--version', dest='version', action='store_true', help='show the version and exit')
    parser.add_argument('--db-file', dest='db_file', default=':memory:',
                        help='specify sqlite3 to use as destination, if not specified db will be IN Memory')

    return parser.parse_args()


def setup_logging(args):
    """Configure logging level by parsing the input parameter"""
    numeric_level = getattr(logging, args.log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.log_level)
    logging.basicConfig(level=numeric_level)


def print_version():
    """Print version and exits"""
    print(VERSION)
    sys.exit(0)
