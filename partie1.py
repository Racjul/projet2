from velociraptor import Velociraptor
from thescelosaurus import Thescelosaurus
from constants import *
from utility import *
from pandas import DataFrame
from matplotlib import pyplot as plt
from partie1.find_stats import simulate_and_plot
from partie1.simulation import run_simulation

if __name__ == "__main__":
    #simulate_and_plot()
    run_simulation(30)