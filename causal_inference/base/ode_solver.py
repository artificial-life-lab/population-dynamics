#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import numpy as np
from scipy import integrate

from causal_inference.config import LV_PARAMS
from causal_inference.base.lv_system import LotkaVolterra

class ODE_solver(LotkaVolterra):
    '''
    This class implements scipy ODE solver for LV system.
    '''
    def __init__(self):
        super().__init__()
        logging.info('Solving Lotka-Volterra predator-prey dynamics odeint solver')

    @staticmethod
    def LV_derivative(X, t, alpha, beta, delta, gamma):
        x, y = X
        dotx = x * (alpha - beta * y)
        doty = y * (-delta + gamma * x)
        return np.array([dotx, doty])

    def _solve(self):
        logging.info('Computing population over time...')
        t = np.arange(0.,self.max_iterations, self.step_size)
        X0 = [self.prey_population, self.predator_population]
        res = integrate.odeint(self.LV_derivative, X0, t, args=(self.A, self.B, self.C, self.D))
        prey_list, predator_list = res.T
        logging.info('done!')
        return prey_list, predator_list