#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Default config variables which maybe overridden by a user config.
'''
import os.path as osp

# Lotka-Volterra Parameters
LV_PARAMS = {
'A' : 10.0,
'B' : 7.0,
'C' : 3.0,
'D' : 5.0,
'STEP_SIZE' : 0.01,
'INITIAL_TIME' : 0,
'INITIAL_PREY_POPULATION' : 60,
'INITIAL_PREDATOR_POPULATION' : 25,
'MAX_ITERATIONS' : 200
}

# PATHS
PROJECT_PATH = osp.abspath(osp.join(osp.dirname(__file__), '..'))
RESULTS_DIR = osp.join(PROJECT_PATH, 'results')
