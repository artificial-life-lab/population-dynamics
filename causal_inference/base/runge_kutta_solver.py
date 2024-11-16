#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
from causal_inference.base.lotka_volterra.lv_system import LotkaVolterra

class RungeKuttaSolver(LotkaVolterra):
    '''
    This class implements 4th order Runge-Kutta solver.
    '''
    def __init__(self):
        super().__init__()
        logging.info('Solving Lotka-Volterra predator-prey dynamics with 4th order Runge-Kutta method')
        self.prey_list = [self.prey_population]
        self.predator_list = [self.predator_population]

    def compute_prey_rate(self, current_prey, current_predators):
        return self.A * current_prey - self.B * current_prey * current_predators

    def compute_predator_rate(self, current_prey, current_predators):
        return - self.C * current_predators + self.D * current_prey * current_predators
    
    def runge_kutta_update(self, current_prey, current_predators):

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
    
    def _solve(self):
        '''
        Runge-Kutta solver that returns the predator and prey populations at each time step in time series.
        '''
        #initial population
        current_prey, current_predators = self.prey_population, self.predator_population

        logging.info(f'Computing population over {self.total_time} generation with step size of {self.step_size}...')

        for step_idx in self.time_stamps[1:]:
            current_prey, current_predators = self.runge_kutta_update(current_prey, current_predators)
            msg= f'Step: {step_idx} | Prey population: {current_prey} | Predator population: {current_predators}'
            logging.info(msg)
        print('Done!')
        return self.prey_list, self.predator_list