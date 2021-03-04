#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Logs experimental configuration in the log file.
'''
import logging
import causal_inference.config as CF

def log_separator_line():
    '''
    Adds a line to log for easy readability.
    '''
    logging.info('-----------------------------------------------')

def log_LV_params():
    '''
    Logs Lotka-Volterra parameters to logfile.
    '''
    log_separator_line()
    logging.info('Lotka-Volterra parameters:')
    logging.info('A: %d', CF.LV_PARAMS['A'])
    logging.info('B: %d', CF.LV_PARAMS['B'])
    logging.info('C: %d', CF.LV_PARAMS['C'])
    logging.info('D: %d', CF.LV_PARAMS['D'])
    logging.info('INITIAL_PREY_POPULATION: %d', CF.LV_PARAMS['INITIAL_PREY_POPULATION'])
    logging.info('INITIAL_PREDATOR_POPULATION: %d', CF.LV_PARAMS['INITIAL_PREDATOR_POPULATION'])
    logging.info('STEP_SIZE: %f', CF.LV_PARAMS['STEP_SIZE'])
    log_separator_line()
