#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Default config variables which maybe overridden by a user config.
'''
import os.path as osp

# Lotka-Volterra Parameters
LV_PARAMS = {
'A' : 1.0,
'B' : 0.1,
'C' : 0.3,
'D' : 0.4,
'STEP_SIZE' : 0.01,
'TOTAL_TIME' : 10,
'INITIAL_PREY_POPULATION' : 40,
'INITIAL_PREDATOR_POPULATION' : 25,
'MAX_ITERATIONS' : 100
}

# PATHS
PROJECT_PATH = osp.abspath(osp.join(osp.dirname(__file__), '..'))
RESULTS_DIR = osp.join(PROJECT_PATH, 'results')
