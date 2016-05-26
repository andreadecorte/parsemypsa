#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
from parsemypsa import _version
    

config = {
    'name': 'parsemypsa',
    'description': 'ParseMyPSA parses files exported from LinkMyPeugeot app',
    'author': 'Andrea Decorte',
    'url': 'https://github.com/klenje/parsemypsa',
    'download_url': 'https://github.com/klenje/parsemypsa',
    #'author_email': 'My email.',
    'version': _version.__version__,
    'license': 'MIT',
    'platforms': 'ALL',
    'install_requires': ['peewee>=2.8.1', 'prompt-toolkit>=1.0'],
    'packages': ['parsemypsa', 'parsemypsa.parsing_input', 'parsemypsa.storage', 'parsemypsa.output'],
    'classifiers': [
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System:: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],

    'scripts': [],

    'entry_points': {
        'console_scripts': [
            'parsemypsa=parsemypsa.main:main',
        ],
    },
}

setup(**config) 
