==========
ParseMyPSA
==========
``parsemypsa`` has the purpose of analyzing the export files of LinkMyPeugeot app. It includes for now a
fixed selection of metrics.

This is **NOT AN OFFICIAL tool** and it's not linked in any way to Peugeot.

Requirements
============
* `Python <http://www.python.org`_
* `peewee <https://github.com/coleifer/peewee>`_
* `prompt-toolkit <https://github.com/jonathanslenders/python-prompt-toolkit>`_

Installation
============

How to use
==========
python main.py --help
usage: main.py [-h] [--log-level LOG_LEVEL] [--version] [--db-file DB_FILE] [input_file]

Parse files produced by LinkMyPeugeot App.

positional arguments:
  input_file            input file to parse

optional arguments:
  -h, --help            show this help message and exit
  --log-level LOG_LEVEL
                        logging level (e.g. DEBUG)
  --version             show the version and exit
  --db-file DB_FILE     specify sqlite3 to use as destination, if not
                        specified db will be IN Memory

Special thanks
==============
Merci to Peugeot IT, because your app crashes badly at startup and so you motivated me to write this
and analyse properly my data :-)