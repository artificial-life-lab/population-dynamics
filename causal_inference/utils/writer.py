#!/usr/bin/python
# -*- coding: utf-8 -*-
from os.path import join
import h5py

def _save_population(prey_list, predator_list, time_stamps, results_dir):
    filename = join(results_dir, 'populations.h5')
    hf = h5py.File(filename, 'w')
    hf.create_dataset('time_stamp', data=time_stamps)
    hf.create_dataset('prey_pop', data=prey_list)
    hf.create_dataset('pred_pop', data=predator_list)
    hf.close()
