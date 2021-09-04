'''
This script computes the amount of levels per difficulty,
saves a table with
'''
import click
import json
import glob
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

difficulties = ["easy", "medium_easy", "medium", "medium_hard", "hard"] 
def compute_amounts(filepath):
    # Creating the folders
    amounts = {
        diff: 0 for diff in difficulties
    }

    with open(filepath) as fp:
        generation = json.load(fp)
    
    for doc in generation.values():
        if doc["performance"] is not None:
            results = doc["metadata"]
            wins = results["wins"]
            winrate = sum(wins) / len(wins)

            if winrate < 0.2:
                amounts["hard"] += 1
                
            elif 0.2 <= winrate < 0.4:
                amounts["medium_hard"] += 1
                
            elif 0.4 <= winrate < 0.6:
                amounts["medium"] += 1
                
            elif 0.6 <= winrate < 0.8:
                amounts["medium_easy"] += 1
                
            elif 0.8 <= winrate <= 1:
                amounts["easy"] += 1
    
    return amounts

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


df = pd.DataFrame(columns=difficulties)
for name, filepath in generations.items():
    amounts = compute_amounts(filepath)
    df.loc[name] = amounts

totals = [
    sum(df.loc[name]) for name in df.index
]
df["totals"] = totals

print(df)
with open("./zelda_experiments/final_tables/levels_segmented_difficulty.csv", "w") as fp:
    fp.write(df.to_csv())

with open("./zelda_experiments/final_tables/levels_segmented_difficulty_tex.txt", "w") as fp:
    fp.write(df.to_latex())

for name in df.index:
    df.loc[name].plot.bar()
    plt.show()

