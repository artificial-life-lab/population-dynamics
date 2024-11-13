#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from causal_inference.config import LV_PARAMS

class LotkaVolterra():
    '''
    Base Lotka-Volterra Class that defines a predator-prey system.
    '''
    def __init__(self,
                 A=LV_PARAMS['A'], B=LV_PARAMS['B'], C=LV_PARAMS['C'], D=LV_PARAMS['D'],
                 prey_population=LV_PARAMS['INITIAL_PREY_POPULATION'],
                 pred_population=LV_PARAMS['INITIAL_PREDATOR_POPULATION'],
                 total_time=LV_PARAMS['TOTAL_TIME'], step_size=LV_PARAMS['STEP_SIZE'],
                 max_iter=LV_PARAMS['MAX_ITERATIONS']):
        # Lotka-Volterra parameters
        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.prey_population = prey_population          # Initial prey population
        self.predator_population = pred_population      # Initial predator population

        self.init_time = 0                       # initial time
        self.total_time = total_time        # total time in units
        self.step_size = step_size          # increment for each time step
        self.max_iterations = max_iter      # tolerance parameter

        self.time_stamps = np.arange(self.init_time, self.total_time, self.step_size)
