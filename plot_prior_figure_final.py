"""
This script gets all the necessary plots for making
the big prior summary figure in Inkscape.
"""

import json
import glob
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import os

from visualization_utils import plot_best_level, plot_mean_winrate

space_coverage = [0.3, 1]
reachability = [0.5, 20.5]
leniency = [-0.5, 15]

partition_3 = {
    "space coverage": space_coverage,
    "reachability": reachability
}

partition_2 = {
    "leniency": leniency,
    "reachability": reachability
}

partition_1 = {
    "space coverage": space_coverage,
    "leniency": leniency
}

all_partitions = {
    **partition_1,
    **partition_2
}

all_keys = list(all_partitions.keys())
all_keys.sort()
print(all_keys)

def plot_prior(generation, prior_name, size=250):
    path_to_prior = f"./zelda_experiments/final_plots/prior_viz/{prior_name}"
    if not os.path.exists(path_to_prior):
        os.makedirs(path_to_prior)
    
    for partition in [partition_1, partition_2, partition_3]:
        _, ax = plt.subplots(1, 1, figsize=(5,5))
        plot_mean_winrate(ax, generation, partition, size=size, plot_labels=False, plot_colorbar=False)
        keys = list(partition.keys())
        keys.sort()
        plt.savefig(f"{path_to_prior}/{keys[0]}_{keys[1]}.jpg", dpi=150, bbox_inches="tight")
        plt.close()
    
    _, ax = plt.subplots(1, 1, figsize=(5,5))
    plot_best_level(ax, generation, winrate_as_title=True)
    plt.savefig(f"{path_to_prior}/best_level.jpg", dpi=150, bbox_inches="tight")
    plt.close()

prior_files = {
        "olets": "./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "MCTS": "./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "RHEA": "./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "RS": "./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "GTS": "./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "OSLA": "./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "Random": "./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "doNothing": "./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        # "baselineRandom": "./zelda_experiments/generations/generation_baselineRandomPrior_00009.json"
    }

font = {'size'   : 16}
matplotlib.rc('font', **font)

for prior_name, filepath in prior_files.items():
    with open(filepath) as fp:
        generation = json.load(fp)
    print(f"For {prior_name}")
    plot_prior(generation, prior_name, size=300)
