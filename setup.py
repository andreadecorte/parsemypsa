#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
from parsemypsa import _version
    

config = {
    'description': 'ParseMyPSA parses files exported from LinkMyPeugeot app',
    'author': 'Andrea Decorte',
    'url': 'https://github.com/klenje/parsemypsa',
    'download_url': 'https://github.com/klenje/parsemypsa',
    #'author_email': 'My email.',
    'version': _version.__version__,
    'install_requires': ['nose'],
    'packages': ['parsemypsa'],
    'scripts': [],
    'name': 'parsemypsa',
    'entry_points': {
        'console_scripts': [
            'parsemypsa=parsemypsa.main:main',
        ],
    },
}

setup(**config) 
