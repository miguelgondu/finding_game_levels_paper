import click
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from operator import itemgetter
from itertools import combinations
from pathlib import Path

from visualization_utils import save_level_from_array

def compute_winrate_performance(generation, key_x, key_y):
    point_winrate_performance = {}
    for k, doc in generation.items():
        if doc["performance"] is None:
            continue
        else:
            if isinstance(doc["features"], (list, tuple, np.ndarray)):
                index_x, index_y = key_x, key_y
            elif isinstance(doc["features"], dict):
                # Sort the keys in doc["features"]
                keys = list(doc["features"].keys())
                keys.sort()

                # Pick the index_x and index_y according to the positions
                # of key_x and key_y in the sorted array, because the
                # centroid was built in alphabetical order.
                index_x, index_y = keys.index(key_x), keys.index(key_y)
            else:
                raise RuntimeError(f"Features is of unexpected type {type(doc['features'])}")

            point = (doc["centroid"][index_x], doc["centroid"][index_y])
            winrate = sum(doc["metadata"]["wins"])/len(doc["metadata"]["wins"])

            if point not in point_winrate_performance:
                point_winrate_performance[point] = (winrate, doc["performance"])

            if point_winrate_performance[point][1] < doc["performance"]:
                point_winrate_performance[point] = (winrate, doc["performance"])
    
    return point_winrate_performance


def plot_winrate(ax, generation, partition, vmin=0, vmax=1, title=""):
    '''
    This function plots the winrate in an axis according to a partition.
    '''
    partition_items = list(partition.items())
    partition_items.sort(key=itemgetter(0))

    key_x = partition_items[0][0]
    key_y = partition_items[1][0]
    xlims = partition_items[0][1][:2]
    ylims = partition_items[1][1][:2]

    # Computing the point_winrate_performance dict
    point_winrate_performance = compute_winrate_performance(generation, key_x, key_y)
    
    # Computing the points and the colors
    points = []
    winrates = []
    for point, winrate in point_winrate_performance.items():
        points.append(point)
        winrates.append(winrate[0])

    points = np.array(points)
    winrates = np.array(winrates)

    scatter = ax.scatter(points[:, 0], points[:, 1], c=winrates, vmin=vmin, vmax=vmax, s=500, marker="s")
    ax.set_xlim(xlims)
    ax.set_ylim(ylims)
    plt.colorbar(scatter, ax=ax)

    if isinstance(partition_items[0][0], str):
        ax.set_xlabel(partition_items[0][0])
        ax.set_ylabel(partition_items[1][0])
    ax.set_title("Winrates" + title)

def plot_performance(ax, generation, partition, vmin=0, vmax=1):
    '''
    This function plots the winrate in an axis according to a partition.
    '''
    partition_items = list(partition.items())
    partition_items.sort(key=itemgetter(0))

    key_x = partition_items[0][0]
    key_y = partition_items[1][0]
    xlims = partition_items[0][1][:2]
    ylims = partition_items[1][1][:2]

    # Computing the point_winrate_performance dict
    point_winrate_performance = compute_winrate_performance(generation, key_x, key_y)
    
    # Computing the points and the colors
    points = []
    performances = []
    for point, tuple_ in point_winrate_performance.items():
        points.append(point)
        performances.append(tuple_[1])

    points = np.array(points)
    performances = np.array(performances)

    scatter = ax.scatter(points[:, 0], points[:, 1], c=performances, vmin=vmin, vmax=vmax, s=500)
    ax.set_xlim(xlims)
    ax.set_ylim(ylims)
    plt.colorbar(scatter, ax=ax)

    if isinstance(partition_items[0][0], str):
        ax.set_xlabel(partition_items[0][0])
        ax.set_ylabel(partition_items[1][0])
    ax.set_title("Performance")

def get_best_performers(generation):
    best_performers = []
    for doc in generation.values():
        if doc["performance"] == 1:
            best_performers.append(doc)
    
    return best_performers

def get_levels_for_winrate(generation, lower, upper):
    """ Returns the cells that had a winrate between lower and upper"""
    docs = []
    for doc in generation.values():
        if doc["performance"] is not None:
            wins = doc["metadata"]["wins"]
            winrate = sum(wins)/len(wins)
            if lower <= winrate < upper:
                docs.append(doc)
    
    return docs

def process_generation(filepath, experiment_name, all_partitions):
    '''
    This function grabs a filepath to a generation.json file
    and process it. By processing it I mean:
    1. Extracting the best performing behaviors, and plotting their levels.
    2. Getting a winratio map for all combinations of features.
    3. Extracting the levels that were easy, medium and hard.
    '''
    with open(filepath) as fp:
        generation = json.load(fp)

    # Creating the necessary folders
    path_summaries = "./zelda_experiments/summaries"
    Path(path_summaries).mkdir(parents=True, exist_ok=True)

    path_summary = f"{path_summaries}/{experiment_name}"
    Path(path_summary).mkdir(parents=True, exist_ok=True)
    # if not os.path.exists(path_summary):
    #     os.makedirs(path_summary)

    path_level_images = f"{path_summary}/best_levels_plotted"
    if not os.path.exists(path_level_images):
        os.makedirs(path_level_images)

    path_results = f"{path_summary}/best_levels_results"
    if not os.path.exists(path_results):
        os.makedirs(path_results)
    
    path_winrates = f"{path_summary}/winrates"
    if not os.path.exists(path_winrates):
        os.makedirs(path_winrates)

    path_easy = f"{path_summary}/easy_levels"
    if not os.path.exists(path_easy):
        os.makedirs(path_easy)

    path_medium = f"{path_summary}/medium_levels"
    if not os.path.exists(path_medium):
        os.makedirs(path_medium)

    path_hard = f"{path_summary}/hard_levels"
    if not os.path.exists(path_hard):
        os.makedirs(path_hard)
    
    # Plotting the best performing levels and
    # saving the best performing results.
    best_performers = get_best_performers(generation)
    for doc in best_performers:
        # Save level with name given by experiment id
        level = np.array(doc["solution"])
        experiment_id = doc["metadata"]["experiment_id"]
        save_level_from_array(level, f"{path_level_images}/{experiment_id}.jpg")
        
        # Save the best performing results.
        with open(f"{path_results}/{experiment_id}.json", "w") as fp:
            json.dump(doc["metadata"], fp)

    # Saving all the winratios
    all_keys = set(all_partitions.keys())
    all_combinations = combinations(all_keys, 2)
    for combination in all_combinations:
        feature_1, feature_2 = combination
        partition = {
            feature_1: all_partitions[feature_1],
            feature_2: all_partitions[feature_2]
        }

        # Plotting winrate
        _, ax = plt.subplots(1, 1, figsize=(10,10))
        plot_winrate(ax, generation, partition, title=experiment_name)
        plt.savefig(f"{path_winrates}/{feature_1.replace(' ', '_')}_{feature_2.replace(' ', '_')}.jpg")
        plt.close()
    
    # Storing the easy, medium and hard levels
    difficulties = {
        path_easy: get_levels_for_winrate(generation, 0.8, 1.1),
        path_medium: get_levels_for_winrate(generation, 0.4, 0.8),
        path_hard: get_levels_for_winrate(generation, -0.1, 0.4)
    }

    for path, docs in difficulties.items():
        print(f"{path}: {len(docs)}")
        for doc in docs:
            level = np.array(doc["solution"])
            experiment_id = doc["metadata"]["experiment_id"]
            wins = doc["metadata"]["wins"]
            winrate = sum(wins)/len(wins)
            save_level_from_array(
                level,
                f"{path}/{experiment_id}.jpg",
                title=f"Winrate: {winrate}"
            )

# @click.command()
# @click.argument("filepath", type=str)
# @click.option("--experiment_name", type=str, default="")
def main():
    # filepath = "zelda_experiments/generations/generation_03_03_2020_random_10_gen_100_iter_17_seed_00009.json"
    # experiment_name = "03_03_2020_random"
    experiments = {
        # "./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json": "olets",
        "./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json": "doNothing",
        # "./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json": "greedyTreeSearch",
        # "./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json": "sampleMCTS",
        # "./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json": "sampleonesteplookahead",
        # "./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json": "sampleRandom",
        # "./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json": "sampleRHEA",
        # "./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json": "sampleRS",
    }
    all_partitions = {
        "space coverage": [0.3, 1],
        "leniency": [-0.5, 11],
        "reachability": [3.5, 16.5]
    }
    for path_, name in experiments.items():
        print(f"Processing: {name}")
        process_generation(path_, name, all_partitions)

if __name__ == "__main__":
    main()