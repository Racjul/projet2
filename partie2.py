import pygame
import math
import sys
from utility import *

from velociraptor import Velociraptor
from thescelosaurus import Thescelosaurus
from constants import *
from partie2.simulation import run_simulation
from partie2.find_stats import simulate_and_plot, find_optimal_distance

if __name__ == "__main__":
    #run_simulation(25)
    simulate_and_plot(192,plot=True)
    #find_optimal_distance()
    #print(angle_between_points(pos_predator_A, pos_prey)*2+2*math.pi)