#!/usr/bin/env python

import logging
import sys

import pytest

from parsemypsa import main


def test_argparse():
    # Clear args
    sys.argv.clear()
    # First is program name
    sys.argv.append("parseMyPSA")
    # Then positional arguments
    sys.argv.append("aa.trip")
    args = main.option_parser()
    assert args.input_file == "aa.trip"


def test_setup_logging():
    # Clear args
    sys.argv.clear()
    # First is program name
    sys.argv.append("parseMyPSA")
    # Then positional arguments
    sys.argv.append("aa.trip")
    # Then optional arguments
    sys.argv.append("--log-level=DEBUG")
    args = main.option_parser()
    assert args.log_level == "DEBUG"
    main.setup_logging(args)
    # TODO fix unfortunately this is broken if run after test in test_console_ui
    # using capsys... to be investigated....
    #assert logging.getLogger("main.py").isEnabledFor(logging.DEBUG)


def test_setup_logging_invalid_value():
    # Clear args
    sys.argv.clear()
    # First is program name
    sys.argv.append("parseMyPSA")
    # Then positional arguments
    sys.argv.append("aa.trip")
    # Then optional argiments
    sys.argv.append("--log-level=DUMMY")
    args = main.option_parser()
    assert args.log_level == "DUMMY"
    with pytest.raises(ValueError):
        main.setup_logging(args)
        assert not logging.getLogger().isEnabledFor(logging.DEBUG)


def test_version():
    # Clear args
    sys.argv.clear()
    # First is program name
    sys.argv.append("parseMyPSA")
    sys.argv.append("--version")
    with pytest.raises(SystemExit) as excinfo:
        main.main()
        assert excinfo.code == 0


def test_input_file_not_found():
    # Clear args
    sys.argv.clear()
    # First is program name
    sys.argv.append("parseMyPSA")
    # Then positional arguments
    sys.argv.append("test.trip")
    args = main.option_parser()
    assert args.input_file == "test.trip"
    with pytest.raises(FileNotFoundError):
        _ = main.file_opener(args)


def test_input_file_not_specified():
    # Clear args
    sys.argv.clear()
    # First is program name
    sys.argv.append("parseMyPSA")
    # No positional arguments
    args = main.option_parser()
    assert args.input_file == None
    with pytest.raises(SystemExit):
        _ = main.file_opener(args)
