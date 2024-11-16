# Population dynamics

[![License](https://img.shields.io/pypi/l/causal-inference-population-dynamics.svg?color=green)](https://github.com/artificial-life-lab/population-dynamics/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/causal-inference-population-dynamics.svg?color=green)](https://pypi.org/project/causal-inference-population-dynamics)
[![codecov](https://codecov.io/gh/artificial-life-lab/population-dynamics/branch/master/graph/badge.svg?token=3SHJIARPOG)](https://codecov.io/gh/artificial-life-lab/population-dynamics)

Library to conduct experiements on population dynamics.

![Lotka-Volterra predator-prey system](docs/graphics/predator_prey.png)

## Installation

- To generate required log and results directories and setup virtual environment, run

```(bash)
bash init.sh
```
This step needs to be performed only once to set up your work space.

- Alternatively, you can create virtual environment manually as follows:

```bash
mkdir -p ~/venvs/population-dynamics
python3 -m venv ~/venvs/population-dynamics
```

- Activate virtual environment
```bash
source ~/venvs/population-dynamics/bin/activate
```

- Upgrade pip and setuptools
```bash
pip install --upgrade pip setuptools
```

- install dependencies with
```bash
pip install -r requirements.txt
```
Alternatively, there exists `requirements_lock.txt` to get a version of the environment that is tested by us in terms of dependencies. The downside of using this file to installing dependencies is that you might not get all the latest version of packages.
In case, if either or the files do not setup the environment successfully, please raise an issue.

- Install `causal_inference` as a package within the environment in development setting if you want to use the repo in the development mode by running the following line

```(bash)
python setup.py develop
```

## Running the Lotka-Volterra simulation

- The Lotka-Volterra simulator class exists in `repo/causal_inference/base/lv_simulator.py`.
- The Lotka-Volterra simulation parameters are fetched from `repo/causal_inference/config.py`.
You can edit the `config.py` file directly to play around with the parameter values.

- You can run the simulator directly from terminal by running

```(bash)
python causal_inference/base/lv_simulator.py
```
This will take all the default arguments and configuration to run a simulation instance of lotka-volterra population dynamics.

- The simulation statistics will be saved in the `repo/results` directory by default.

## Simulation and inference

- The simulation and inference methods are separately implemented in `repo/causal_inference/base/lotka_volterra/lv_system.py`.
- Currently, this inference method is experimental and may not always converge to correct optimal parameters.
- More work is needed to find a good approximation schema to initiate the parameters of the LV-system.
