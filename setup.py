#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name="markov-algorithm-interpreter",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'markov = markov_algorithm:main',
        ],
    },
)
