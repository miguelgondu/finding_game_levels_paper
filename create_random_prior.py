"""
This script creates a random prior by alterating the
doNothing prior, using random performances.
"""

import json
import numpy as np
import matplotlib.pyplot as plt
import pymelites
from zelda_map_elites_utils import random_solution, compute_features
from visualization_utils import plot_mean_performance, plot_mean_winrate, plot_level_from_array

partition_3 = {
    "space coverage": [0.3, 1],
    "reachability": [3.5, 16.5]
}

partition_2 = {
    "leniency": [-0.5, 11.5],
    "reachability": [3.5, 16.5]
}

partition_1 = {
    "space coverage": [0.3, 1],
    "leniency": [-0.5, 11.5]
}

# Load the original doNothing prior
with open("./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json") as fp:
    generation = json.load(fp)

# Modify it
for doc in generation.values():
    if doc["performance"] is not None:
        doc["performance"] = np.random.uniform()

_, ax = plt.subplots(1, 1, figsize=(10, 10))
plot_mean_performance(ax, generation, partition_1)
plt.show()

with open("./zelda_experiments/generations/generation_baselineRandomPrior_00009.json", "w") as fp:
    json.dump(generation, fp)
