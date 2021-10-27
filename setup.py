#!/usr/bin/env python3
# flake8: noqa
'''
Setup script for the repository.
'''
from setuptools import find_packages, setup, Distribution


requirements = []
with open('requirements.txt') as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

# Currently incompatible with PyPi
# use_scm = {"write_to": "causal_inference/_version.py"}

def local_scheme(version):
    return ""

long_description = """

# Causal-inference-population-dynamics

Causal-inference-population-dynamics is a library to simulate and infer population dynamics models.

The currently imlemented population dynamics models are
+ Lotka-Volterra model

## Running the code

You can run the simulator directly from terminal by running

```(bash)
python causal/base/lotka_volterra.py
```

The simulation statistics will be saved in the `repo/results` directory.

"""

setup(
    name = 'causal-inference-population-dynamics',
    author='Pranjal Dhole',
    author_email='dhole.pranjal@gmail.com',
    license='MIT',
    url='https://github.com/artificial-life-lab/population-dynamics',
    description='Library to conduct experiments in population dynamics.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    distclass = Distribution,
    packages = find_packages(),
    python_requires='>=3.7',
    install_requires=requirements,
    version='1.0.2',
    setup_requires=['setuptools_scm'],
    # PyPI package information.
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
