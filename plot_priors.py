"""
This script plots the paper-ready version of the priors:
three 2x4 plots with all the priors for the 3 combinations.
"""
import json
import matplotlib.pyplot as plt
from visualization_utils import plot_mean_winrate

all_partitions = {
    "space coverage": [0.3, 1],
    "leniency": [-0.5, 11.5],
    "reachability": [3.5, 16.5],
}

partition_3 = {"space coverage": [0.3, 1], "reachability": [3.5, 16.5]}

partition_2 = {"leniency": [-0.5, 11.5], "reachability": [3.5, 16.5]}

partition_1 = {"space coverage": [0.3, 1], "leniency": [-0.5, 11.5]}

size = 250
font_size = 20
label_font_size = 28

for partition in [partition_1, partition_2, partition_3]:
    figure_name = "_".join(partition.keys()).replace(" ", "_")

    plt.rcParams.update({"font.size": font_size})

    fig, axes = plt.subplots(1, 8, figsize=(80 // 2, 10 // 2), sharex=True, sharey=True)

    with open(
        "./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json"
    ) as fp:
        doNothing = json.load(fp)
    plot_mean_winrate(
        axes[0], doNothing, partition, size=size, plot_labels=False, plot_colorbar=False
    )
    axes[0].set_title("DoNothing")

    with open(
        "./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json"
    ) as fp:
        sampleRandom = json.load(fp)
    plot_mean_winrate(
        axes[1],
        sampleRandom,
        partition,
        size=size,
        plot_labels=False,
        plot_colorbar=False,
    )
    axes[1].set_title("Random")

    with open(
        "./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json"
    ) as fp:
        sampleonesteplookahead = json.load(fp)
    plot_mean_winrate(
        axes[2],
        sampleonesteplookahead,
        partition,
        size=size,
        plot_labels=False,
        plot_colorbar=False,
        return_scatter=True,
    )
    axes[2].set_title("one-step lookahead")

    with open(
        "./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json"
    ) as fp:
        greedyTreeSearch = json.load(fp)
    plot_mean_winrate(
        axes[3],
        greedyTreeSearch,
        partition,
        size=size,
        plot_labels=False,
        plot_colorbar=False,
    )
    axes[3].set_title("Greedy Tree Search")

    with open(
        "./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json"
    ) as fp:
        sampleRHEA = json.load(fp)
    plot_mean_winrate(
        axes[4],
        sampleRHEA,
        partition,
        size=size,
        plot_labels=False,
        plot_colorbar=False,
    )
    axes[4].set_title("RHEA")

    with open(
        "./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json"
    ) as fp:
        sampleRS = json.load(fp)
    plot_mean_winrate(
        axes[5], sampleRS, partition, size=size, plot_labels=False, plot_colorbar=False
    )
    axes[5].set_title("Random Search")

    with open(
        "./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json"
    ) as fp:
        sampleMCTS = json.load(fp)
    plot_mean_winrate(
        axes[6],
        sampleMCTS,
        partition,
        size=size,
        plot_labels=False,
        plot_colorbar=False,
    )
    axes[6].set_title("MCTS")

    with open(
        "./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json"
    ) as fp:
        olets = json.load(fp)
    scatter = plot_mean_winrate(
        axes[7],
        olets,
        partition,
        size=size,
        plot_labels=False,
        plot_colorbar=False,
        return_scatter=True,
    )
    axes[7].set_title("OLETS")

    # fig.subplots_adjust(right=0.8)
    # cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    # fig.colorbar(scatter, cax=cbar_ax)
    # fig.colorbar(scatter)
    # plt.suptitle("Mean winrate per agent", fontsize=45)

    keys = list(partition.keys())
    keys.sort()

    # fig.text(0.45, -0.03, "\n\n\n" + keys[0], ha='center', fontsize=label_font_size)
    axes[3].set_xlabel(" " * 5 + keys[0], fontsize=label_font_size)
    # fig.text(0.09, 0.5, keys[1], va='center', rotation='vertical', fontsize=label_font_size)
    axes[0].set_ylabel(keys[1], fontsize=label_font_size)
    plt.tight_layout()
    # plt.show()
    plt.savefig(f"./zelda_experiments/final_plots/{figure_name}.jpg", dpi=200)
