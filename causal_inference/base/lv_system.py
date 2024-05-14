#!/usr/bin/python
# -*- coding: utf-8 -*-

from causal_inference.config import LV_PARAMS

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