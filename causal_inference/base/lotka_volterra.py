#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os
import logging
import datetime
import h5py
import matplotlib.pyplot as plt

from causal_inference.config import LV_PARAMS, RESULTS_DIR
from causal_inference.utils.log_config import log_LV_params


class LotkaVolterra():
    '''
    Class simulates predator-prey dynamics and solves it with 4th order Runge-Kutta method.
    '''
    def __init__(self):
        self.A = LV_PARAMS['A']
        self.B = LV_PARAMS['B']
        self.C = LV_PARAMS['C']
        self.D = LV_PARAMS['D']
        self.time = LV_PARAMS['INITIAL_TIME']
        self.step_size = LV_PARAMS['STEP_SIZE']
        self.max_iterations = LV_PARAMS['MAX_ITERATIONS']

        self.prey_population = LV_PARAMS['INITIAL_PREY_POPULATION']
        self.predator_population = LV_PARAMS['INITIAL_PREDATOR_POPULATION']

        self.time_stamp = [self.time]
        self.prey_list = [self.prey_population]
        self.predator_list = [self.predator_population]
    
    def compute_prey_rate(self, current_prey, current_predators):
        return self.A * current_prey - self.B * current_prey * current_predators

    def compute_predator_rate(self, current_prey, current_predators):
        return - self.C * current_predators + self.D * current_prey * current_predators
    
    def runge_kutta_update(self, current_prey, current_predators):
        self.time = self.time + self.step_size
        self.time_stamp.append(self.time)

        k1_prey = self.step_size * self.compute_prey_rate(current_prey, current_predators)
        k1_pred = self.step_size * self.compute_predator_rate(current_prey, current_predators)

        k2_prey = self.step_size * self.compute_prey_rate(current_prey + 0.5 * k1_prey, current_predators + 0.5 * k1_pred)
        k2_pred = self.step_size * self.compute_predator_rate(current_prey + 0.5 * k1_prey, current_predators + 0.5 * k1_pred)

        k3_prey = self.step_size * self.compute_prey_rate(current_prey + 0.5 * k2_prey, current_predators + 0.5 * k2_pred)
        k3_pred = self.step_size * self.compute_predator_rate(current_prey + 0.5 * k2_prey, current_predators + 0.5 * k2_pred)

        k4_prey = self.step_size * self.compute_prey_rate(current_prey + k3_prey, current_predators + k3_pred)
        k4_pred = self.step_size * self.compute_predator_rate(current_prey + k3_prey, current_predators + k3_pred)

        new_prey_population = current_prey + 1/6 * (k1_prey + 2 * k2_prey + 2 * k3_prey + k4_prey)
        new_predator_population = current_predators + 1/6 * (k1_pred + 2 * k2_pred + 2 * k3_pred + k4_pred)

        self.prey_list.append(new_prey_population)
        self.predator_list.append(new_predator_population)

        return new_prey_population, new_predator_population

    def _save_population(self):
        filename = os.path.join(RESULTS_DIR, 'populations.h5')
        hf = h5py.File(filename, 'w')
        hf.create_dataset('prey_pop', data=self.predator_list)
        hf.create_dataset('pred_pop', data=self.predator_list)
        hf.close()

    def _solve(self):
        current_prey, current_predators = self.prey_population, self.predator_population
        logging.info('Computing population over time...')
        for gen_idx in range(self.max_iterations):
            current_prey, current_predators = self.runge_kutta_update(current_prey, current_predators)
            logging.info('Gen: %d | Prey population: %d | Predator population: %d', gen_idx, current_prey, current_predators)
        print('Done!')
    
    def plot_population_over_time(self, save=True, filename='predator_prey'):
        _ = plt.figure(figsize=(15, 5))
        PreyLine, = plt.plot(self.prey_list , color='g')
        PredatorsLine, = plt.plot(self.predator_list, color='r')
        plt.legend([PreyLine, PredatorsLine], ['Prey', 'Predators'])
        plt.ylabel('Population')
        plt.xlabel('Time')
        if save:
            plt.savefig(os.path.join(RESULTS_DIR, f"{filename}.svg"),
                        format='svg', transparent=False, bbox_inches='tight')
        else:
            plt.show()
        plt.close()

def main():
    logging.info('Lotka-Volterra predator-prey dynamics with 4th order Runge-Kutta method')
    m = LotkaVolterra()
    log_LV_params()
    m._solve()
    m._save_population()
    m.plot_population_over_time()

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-log', '--logfile', help='name of the logfile', default='log')
    PARSER.add_argument('-out', '--outdir', help='Where to place the results', default='lv_simulation')
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

    main()
