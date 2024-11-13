#!/usr/bin/python
# -*- coding: utf-8 -*-
from os.path import join
import matplotlib.pyplot as plt

def plot_population_over_time(prey_list, predator_list, time_stamps, results_dir, save=True, filename='predator_prey'):
    fig = plt.figure(figsize=(15, 5))
    ax = fig.add_subplot(2, 1, 1)
    PreyLine, = plt.plot(time_stamps, prey_list, color='g')
    PredatorsLine, = plt.plot(time_stamps, predator_list, color='r')
    ax.set_xscale('log')

    plt.legend([PreyLine, PredatorsLine], ['Prey', 'Predators'])
    plt.ylabel('Population')
    plt.xlabel('Time')
    if save:
        plt.savefig(join(results_dir, f"{filename}.svg"),
                    format='svg', transparent=False, bbox_inches='tight')
    else:
        plt.show()
    plt.close()