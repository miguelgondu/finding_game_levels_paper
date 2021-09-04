"""
In this script, I plan to implement a gif to visualize the
update process for twitter.
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import json
import glob

# Selected update: sampleRS prior on GTS agent, iteration 0.

path_to_updates = "./zelda_experiments/updates"
path_to_priors = "./zelda_experiments/generations"

# Hm, I should plot all the generations.

generations = list(glob.glob(f"{path_to_priors}/*_sampleRS_*.json"))
generations.sort()

print(generations)

