"""
This script takes the results of an experiment and analyses
1. Segments levels created for a particular experiment depending
   on their winrate.
2. Checks for level collisions, and for the noise in the experiment
   in those level collisions (which, unfortunately, I think will result
   in the same winrates because the inner seeds arent changing).
"""

import click
import json
import glob
import os
import matplotlib.pyplot as plt
import numpy as np

from visualization_utils import save_level_from_txt, save_level_from_array


def segment_levels(filepath, path_to_experiment):
    # Creating the folders
    for folder in ["easy", "medium_easy", "medium", "medium_hard", "hard"]:
        if not os.path.exists(f"{path_to_experiment}/{folder}"):
            os.makedirs(f"{path_to_experiment}/{folder}")

    with open(filepath) as fp:
        generation = json.load(fp)

    for doc in generation.values():
        if doc["performance"] is not None:
            results = doc["metadata"]

            experiment_id = results["experiment_id"]
            level = doc["solution"]
            wins = results["wins"]
            winrate = sum(wins) / len(wins)

            if winrate < 0.2:
                save_level_from_array(
                    level,
                    f"{path_to_experiment}/hard/{experiment_id}.jpg",
                    f"Winrate: {winrate}",
                )
            elif 0.2 <= winrate < 0.4:
                save_level_from_array(
                    level,
                    f"{path_to_experiment}/medium_hard/{experiment_id}.jpg",
                    f"Winrate: {winrate}",
                )
            elif 0.4 <= winrate < 0.6:
                save_level_from_array(
                    level,
                    f"{path_to_experiment}/medium/{experiment_id}.jpg",
                    f"Winrate: {winrate}",
                )
            elif 0.6 <= winrate < 0.8:
                save_level_from_array(
                    level,
                    f"{path_to_experiment}/medium_easy/{experiment_id}.jpg",
                    f"Winrate: {winrate}",
                )
            elif 0.8 <= winrate <= 1:
                save_level_from_array(
                    level,
                    f"{path_to_experiment}/easy/{experiment_id}.jpg",
                    f"Winrate: {winrate}",
                )


# @click.command()
# @click.argument("filepath", type=str, default="")
# @click.option("--experiment_name", type=str, default="MCTS_50_rollouts")
# @click.option("--path_to_seg", type=str, default="./zelda_experiments/levels_segmented")
def segment_generation(filepath, experiment_name, path_to_seg):
    path_to_experiment = f"{path_to_seg}/{experiment_name}"
    segment_levels(filepath, path_to_experiment)


generations = {
    "olets": "./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
    "sampleMCTS": "./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
    "sampleRHEA": "./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
    "sampleRS": "./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
    "greedyTreeSearch": "./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
    "sampleonesteplookahead": "./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
    "sampleRandom": "./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
    "doNothing": "./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
}

path_to_seg = "./zelda_experiments/levels_segmented"
for experiment_name, filepath in generations.items():
    segment_generation(filepath, experiment_name, path_to_seg)
