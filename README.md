# Population dynamics

[![License](https://img.shields.io/pypi/l/causal-inference-population-dynamics.svg?color=green)](https://github.com/artificial-life-lab/population-dynamics/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/causal-inference-population-dynamics.svg?color=green)](https://pypi.org/project/causal-inference-population-dynamics)
[![codecov](https://codecov.io/gh/artificial-life-lab/population-dynamics/branch/master/graph/badge.svg?token=3SHJIARPOG)](https://codecov.io/gh/artificial-life-lab/population-dynamics)

Library to conduct experiements on population dynamics.

![Lotka-Volterra predator-prey system](docs/graphics/predator_prey.png)

## Installation

- To generate required log and results directories, run

```(bash)
bash init.sh
```

- Create virtual environment
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
```

- Install `causal_inference` as a package within the environment

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

- The simulation statistics will be saved in the `repo/results` directory.
