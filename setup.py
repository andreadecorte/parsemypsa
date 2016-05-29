#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os
    
from parsemypsa import _version


def _read(fn):
    path = os.path.join(os.path.dirname(__file__), fn)
    return open(path).read()
    

config = {
    'name': 'parsemypsa',
    'description': 'ParseMyPSA parses files exported from LinkMyPeugeot app',
    'long_description': _read('README.rst'),
    'author': 'Andrea Decorte',
    'url': 'https://github.com/klenje/parsemypsa',
    'download_url': 'https://github.com/klenje/parsemypsa',
    # 'author_email': 'My email.',
    'version': _version.__version__,
    'license': 'MIT',
    'platforms': 'ALL',
    'install_requires': ['peewee>=2.8.1', 'prompt-toolkit>=1.0'],
    'setup_requires': ['pytest-runner'],
    'test_requires': ['pytest>=2.9.1'],
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
