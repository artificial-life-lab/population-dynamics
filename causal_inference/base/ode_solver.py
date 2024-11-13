#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import numpy as np
from scipy import integrate

from causal_inference.base.lv_system import LotkaVolterra

class ODE_solver(LotkaVolterra):
    '''
    This class implements scipy ODE solver for LV system.
    '''
    def __init__(self):
        super().__init__()
        logging.info('Simulating Lotka-Volterra predator-prey dynamics with odeint solver')

    @staticmethod
    def LV_derivative(t, Z, A, B, C, D):
        '''
        Returns the rate of change of predator and prey population
        '''
        x, y = Z
        dotx = x * (A - B * y)
        doty = y * (-C + D * x)
        return np.array([dotx, doty])

    def _solve(self):
        '''
        ODE solver that returns the predator and prey populations at each time step in time series.
        '''
        logging.info(f'Computing population over {self.total_time} generation with step size of {self.step_size}...')

        INIT_POP = [self.prey_population, self.predator_population]
        sol = integrate.solve_ivp(self.LV_derivative, [self.init_time, self.total_time], INIT_POP, args=(self.A, self.B, self.C, self.D), dense_output=True)
        prey_list, predator_list = sol.sol(self.time_stamps)

        logging.info('done!')

        return prey_list, predator_list
