#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import integrate
from scipy.optimize import minimize

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

        self.init_time = 0                  # initial time
        self.total_time = total_time        # total time in units
        self.step_size = step_size          # increment for each time step
        self.max_iterations = max_iter      # tolerance parameter

        self.time_stamps = np.arange(self.init_time, self.total_time, self.step_size)

@staticmethod
def LV_derivative(t, Z, A, B, C, D):
    '''
    Returns the rate of change of predator and prey population

    Simulates Lotka-Volterra dynamics

    Parameters:
    t (list): [t0, tf] initial and final time points for simulation (Not used but necessary for integration step)
    Z (tuple): (x, y) state of the system
    A: prey growth rate (model parameter)
    B: predation rate (model parameter)
    C: predator death rate (model parameter)
    D: predator growth rate from eating prey (model parameter)

    Returns:
    array: rate of change of prey and predator population
    '''
    x, y = Z
    dotx = x * (A - B * y)
    doty = y * (-C + D * x)
    return np.array([dotx, doty])

def simulate_lotka_volterra(params, t, initial_conditions):
    """
    Simulates Lotka-Volterra dynamics

    Parameters:
    params (tuple): (A, B, C, D) model parameters
        A: prey growth rate
        B: predation rate
        C: predator death rate
        D: predator growth rate from eating prey
    t (array): time points for simulation
    initial_conditions (tuple): (prey0, predator0) initial populations

    Returns:
    population: (n, 2) array where each row is [prey_pop, predator_pop]
    """
    A, B, C, D = params

    solution = integrate.solve_ivp(LV_derivative, [t[0], t[-1]], initial_conditions,
                                   args=(A, B, C, D), dense_output=True)
    
    population = solution.sol(t)
    return population

def fit_lotka_volterra(time_points, observed_data, initial_guess):
    """
    Fits Lotka-Volterra parameters to observed population data

    Parameters:
    time_points (array): time points of observations
    observed_data (array): observed population data [prey, predator]
    initial_guess (tuple): initial parameter guess (A, B, C, D)

    Returns:
    tuple: Fitted parameters (A, B, C, D) after optimization
    """
    def objective_function(params):
        # Simulate with current parameters
        simulated = simulate_lotka_volterra(params, time_points,
                                            observed_data[:, 0])
        # Calculate mean squared error
        mse = np.mean((simulated - observed_data) ** 2)
        return mse

    # Parameter bounds (all parameters must be positive)
    bounds = [(0, None) for _ in range(4)]

    # Optimize parameters
    result = minimize(objective_function, initial_guess,
                      bounds=bounds, method='L-BFGS-B')

    return result.x

# Example usage:
if __name__ == "__main__":
    # Generate synthetic data
    m = LotkaVolterra()
    true_params = (m.A, m.B, m.C, m.D)
    initial_conditions = (m.prey_population, m.predator_population)     # (prey0, predator0)

    # Generate synthetic data with some noise
    data = simulate_lotka_volterra(true_params, m.time_stamps, initial_conditions)
    noisy_data = data + np.random.normal(0, 0.1, data.shape)

    # Fit parameters
    initial_guess = (0.5, 0.05, 0.05, 0.05) #FIXME Use more educated schema for initial guess

    fitted_params = fit_lotka_volterra(m.time_stamps, noisy_data, initial_guess)

    print("True parameters:", true_params)
    print("Fitted parameters:", fitted_params)
