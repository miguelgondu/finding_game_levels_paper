"""
This script plots a big summary with all the priors and all
the best performing levels (i.e. a 8x4 plot).
"""

import json
import glob
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

from visualization_utils import plot_best_level, plot_mean_winrate

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

def plot_row(axes, row, generation, size=250):
    row_axes = axes[row, :]
    plot_mean_winrate(row_axes[0], generation, partition_1, size=size, plot_labels=False, plot_colorbar=False)
    plot_mean_winrate(row_axes[1], generation, partition_2, size=size, plot_labels=False, plot_colorbar=False)
    plot_mean_winrate(row_axes[2], generation, partition_3, size=size, plot_labels=False, plot_colorbar=False)
    plot_best_level(row_axes[3], generation, winrate_as_title=False)


prior_files = {
        "olets": "./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "MCTS": "./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "RHEA": "./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "RS": "./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "GTS": "./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "OSLA": "./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "Random": "./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "doNothing": "./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
    }

font = {'size'   : 14}

matplotlib.rc('font', **font)

base_size = 4
fig, axes = plt.subplots(8, 4, figsize=(4*base_size, 8*base_size))
for row, filepath in enumerate(prior_files.values()):
    with open(filepath) as fp:
        generation = json.load(fp)
    
    plot_row(axes, row, generation, size=55*base_size)


# for ax, col in zip(axes[0], cols):
#     ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
#                 xycoords='axes fraction', textcoords='offset points',
#                 size='large', ha='center', va='baseline')

pad = 5 # in points
agents = prior_files.keys()
for ax, agent in zip(axes[:,0], agents):
    ax.annotate(agent, xy=(0, 0.5), xytext=(-ax.yaxis.labelpad - pad, 0),
                xycoords=ax.yaxis.label, textcoords='offset points',
                size='large', ha='right', va='center')

cols = ["leniency\n vs.\n space coverage", "leniency\n vs.\n reachability", "reachability\n vs.\n space coverage", r"level w. $\approx$ 60% winrate"]
for ax, col in zip(axes[0], cols):
    ax.annotate(col, xy=(0.5, 1), xytext=(0, pad),
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')

axes[-1, -1].set_title("Winrate: 0.0")
# plt.show()
# plt.tight_layout()
plt.savefig("./zelda_experiments/final_plots/big_summary.pdf", dpi=150, bbox_inches="tight")

