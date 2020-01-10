#!/usr/bin/env python3
# flake8: noqa
'''
Setup script for the repository.
'''
from setuptools import find_packages, setup, Distribution
from causal.version import __version__

setup(
    name = 'causal',
    version = __version__,
    distclass = Distribution,
    packages = find_packages(),
    zip_safe = False,
)
