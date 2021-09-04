"""
This script uses the plot_mean_performance from process_updates
to visualize all the priors of all generations.
"""

import click
import glob
import json
import matplotlib.pyplot as plt
import numpy as np

from visualization_utils import plot_mean_winrate, plot_mean_performance

def plot_prior(path, feat_1, feat_2):
    agent_name = path.split("/")[-1].split("_")[1]
    with open(path) as fp:
        generation = json.load(fp)
    
    all_partitions = {
        "space coverage": [0.3, 1],
        "leniency": [-0.5, 12.5],
        "reachability": [2.5, 16.5]
    }

    partition = {
        feat_1: all_partitions[feat_1],
        feat_2: all_partitions[feat_2]
    }

    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    plot_mean_performance(ax1, generation, partition)
    ax1.set_title(f"Mean performance - {agent_name}")
    plot_mean_winrate(ax2, generation, partition)
    ax2.set_title(f"Mean winrate - {agent_name}")
    plt.show()

def plot_all_priors(pattern, feat_1, feat_2, comment=None):
    all_partitions = {
        "space coverage": [0.3, 1],
        "leniency": [-0.5, 12.5],
        "reachability": [2.5, 16.5]
    }

    partition = {
        feat_1: all_partitions[feat_1],
        feat_2: all_partitions[feat_2]
    }

    generation_paths = glob.glob(f"./zelda_experiments/generations/generation_{pattern}_*.json")
    for path in generation_paths:
        agent_name = path.split("/")[-1].split("_")[1]
        iteration = path.split("/")[-1].split(".")[0].split("_")[-1]
        with open(path) as fp:
            generation = json.load(fp)

        _, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
        plot_mean_performance(ax1, generation, partition)
        ax1.set_title(f"Mean \"closeness\" to 0.6 - {agent_name}")
        plot_mean_winrate(ax2, generation, partition)
        ax2.set_title(f"Mean winrate - {agent_name}")
        # plt.show()
        path_to_fig = path.replace("/generations/", "/priors/")
        _list = path_to_fig.split("/")

        if comment:
            _list[-1] = f"prior_{agent_name}_{comment}_{feat_1}_{feat_2}_{iteration}.jpg"
        else:
            _list[-1] = f"prior_{agent_name}_{feat_1}_{feat_2}_{iteration}.jpg"

        path_to_fig = "/".join(_list)
        plt.savefig(path_to_fig, dpi=150)

if __name__ == "__main__":
    plot_all_priors("sampleMCTS", "space coverage", "leniency")