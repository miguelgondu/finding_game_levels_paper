import json
import matplotlib.pyplot as plt
import matplotlib

from visualization_utils import plot_mean_winrate

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

partition_2 = {
    "leniency": [-0.5, 11.5],
    "reachability": [3.5, 16.5]
}

matplotlib.rcParams['axes.linewidth'] = 5 #set the value globally

for i, filepath in enumerate(prior_files.values()):
    with open(filepath) as fp:
        generation = json.load(fp)
    
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    plot_mean_winrate(ax, generation, partition=partition_2, plot_colorbar=False, plot_labels=False)
    # ax.axis("off")
    ax.tick_params(
        top=False,
        bottom=False,
        labelbottom=False,
        right=False,
        left=False,
        labelleft=False,
    )
    plt.savefig(f"./zelda_experiments/final_plots/overview_map_{i}.jpg", dpi=150, bbox_inches="tight")
