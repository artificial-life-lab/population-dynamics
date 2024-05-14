#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os
import logging
import datetime

import h5py
import matplotlib.pyplot as plt

from causal_inference.config import RESULTS_DIR
from causal_inference.utils.log_config import log_LV_params
from causal_inference.base.ode_solver import ODE_solver
from causal_inference.base.runge_kutta_solver import RungeKuttaSolver

def _save_population(prey_list, predator_list):
    filename = os.path.join(RESULTS_DIR, 'populations.h5')
    hf = h5py.File(filename, 'w')
    hf.create_dataset('prey_pop', data=prey_list)
    hf.create_dataset('pred_pop', data=predator_list)
    hf.close()

def plot_population_over_time(prey_list, predator_list, save=True, filename='predator_prey'):
    fig = plt.figure(figsize=(15, 5))
    ax = fig.add_subplot(2, 1, 1)
    PreyLine, = plt.plot(prey_list , color='g')
    PredatorsLine, = plt.plot(predator_list, color='r')
    ax.set_xscale('log')

    plt.legend([PreyLine, PredatorsLine], ['Prey', 'Predators'])
    plt.ylabel('Population')
    plt.xlabel('Time')
    if save:
        plt.savefig(os.path.join(RESULTS_DIR, f"{filename}.svg"),
                    format='svg', transparent=False, bbox_inches='tight')
    else:
        plt.show()
    plt.close()

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

def main(method):
    '''
    Main function that solves LV system.
    '''
    log_LV_params()
    solver = get_solver(method)
    prey_list, predator_list = solver._solve()
    _save_population(prey_list, predator_list)
    plot_population_over_time(prey_list, predator_list)

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-log', '--logfile', help='name of the logfile', default='log')
    PARSER.add_argument('-out', '--outdir', help='Where to place the results', default='lv_simulation')
    PARSER.add_argument('-s', '--solver', help='Mathematical solver for solving LV system',
                        choices=['RK4', 'ODE'], default='RK4')
    ARGS = PARSER.parse_args()

    RESULTS_DIR = os.path.join(RESULTS_DIR, '{}_{}'.format(datetime.datetime.now().strftime("%Y%h%d_%H_%M_%S"), str(ARGS.outdir)))

    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    LOG_FILE = os.path.join(RESULTS_DIR, f"{ARGS.logfile}.txt")     # write logg to this file
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    solver = ARGS.solver
    main(solver)
