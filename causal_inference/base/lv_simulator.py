#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os
import logging
import datetime

from causal_inference.config import RESULTS_DIR
from causal_inference.utils.log_config import log_LV_params
from causal_inference.base.ode_solver import ODE_solver
from causal_inference.base.runge_kutta_solver import RungeKuttaSolver
from causal_inference.utils.writer import _save_population
from causal_inference.utils.visualisations import plot_population_over_time

def get_solver(method):
    '''
    solving LV equation with scipy function.
    '''
    if method == 'RK4':
        solver = RungeKuttaSolver()
    elif method == 'ODE':
        solver = ODE_solver()
    else:
        raise AssertionError(f'{method} is not implemented!')
    return solver

def main(method, results_dir):
    '''
    Main function that solves LV system.
    '''
    log_LV_params()
    solver = get_solver(method)
    prey_list, predator_list = solver._solve()
    _save_population(prey_list, predator_list, solver.time_stamps, results_dir)
    plot_population_over_time(prey_list, predator_list, solver.time_stamps, results_dir)

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-log', '--logfile', help='name of the logfile', default='log')
    PARSER.add_argument('-out', '--outdir', help='Where to place the results', default='lv_simulation')
    PARSER.add_argument('-s', '--solver', help='Mathematical solver for solving LV system',
                        choices=['RK4', 'ODE'], default='RK4')
    ARGS = PARSER.parse_args()

    results_dir = os.path.join(RESULTS_DIR, '{}_{}'.format(datetime.datetime.now().strftime("%Y%h%d_%H_%M_%S"), str(ARGS.outdir)))

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    LOG_FILE = os.path.join(results_dir, f"{ARGS.logfile}.txt")     # write logg to this file
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    solver = ARGS.solver
    main(solver, results_dir)
