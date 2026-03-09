import neat
import os
# We import the pre-coded environment you'll provide them
from environment import Car, Track, draw_window 

def eval_genomes(genomes, config):
    """
    This is the core Fitness Function. 
    It runs one generation of cars and evaluates how well they do.
    """
    nets = []
    cars = []
    genomes_list = []

    # 1. SETUP THE POPULATION
