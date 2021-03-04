#!/usr/bin/env python3
# flake8: noqa
'''
Setup script for the repository.
'''
import os
import codecs
from setuptools import find_packages, setup, Distribution
from causal_inference.version import __version__

def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()

requirements = []
with open('requirements.txt') as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

setup(
    name = 'causal-inference',
    author='Pranjal Dhole',
    author_email='dhole.pranjal@gmail.com',
    licence='MIT',
    url='https://github.com/artificial-life-lab/population-dynamics',
    description='Library to conduct experiments in population dynamics.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    version = __version__,
    distclass = Distribution,
    packages = find_packages(),
    python_requires='>=3.7',
    install_requires=requirements,
    zip_safe = False,
)
