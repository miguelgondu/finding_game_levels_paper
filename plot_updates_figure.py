import glob
import json
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

from visualization_utils import plot_level_from_array, plot_mean_performance
matplotlib.rc('text', usetex=True)

prior = "sampleRandom"
agent = "sampleonesteplookahead"
iteration = 1

# prior = "baselineRandomPrior"
# agent = "sampleRHEA"
# iteration = 6

# prior = "sampleMCTS"
# agent = "sampleRS"
# iteration = 7

# prior = "baselineRandomPrior"
# agent = "sampleRS"
# iteration = 8

filepaths = glob.glob(f"zelda_experiments/updates/{prior}_prior/{agent}/update_2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_{prior}_to_{agent}_iteration_{iteration}__*.json")
# zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00004.json
original_gen_path = glob.glob(f"zelda_experiments/generations/generation_{prior}_*9.json")
assert len(original_gen_path) == 1
original_gen_path = original_gen_path[0]

partition_3 = {
    "space coverage": [0.3, 1],
    "reachability": [3.5, 18.5]
}

partition_2 = {
    "leniency": [-0.5, 11.5],
    "reachability": [3.5, 18.5]
}

partition_1 = {
    "space coverage": [0.3, 1],
    "leniency": [-0.5, 11.5]
}

all_partitions = {
    **partition_1,
    **partition_2
}

partitions = [partition_1, partition_2, partition_3]

all_keys = list(all_partitions.keys())
all_keys.sort()

# matplotlib.rcParams['axes.linewidth'] = 5 #set the value globally
# matplotlib.rcParams['text.size'] = 16 #set the value globally
matplotlib.rc("font", size=16)



with open(original_gen_path) as fp:
    generation = json.load(fp)

matplotlib.rcParams['axes.linewidth'] = 5
for partition in partitions:
    keys = list(partition.keys())
    keys.sort()
    _, ax = plt.subplots(1, 1, figsize=(5,5))
    plot_mean_performance(ax, generation, partition, size=250, plot_colorbar=False)
    ax.tick_params(
        top=False,
        bottom=False,
        labelbottom=False,
        right=False,
        left=False,
        labelleft=False,
    )
    plt.savefig(f"./zelda_experiments/final_plots/update_viz/{keys[0]}_{keys[1]}_original.jpg", dpi=150, bbox_inches="tight")


for path in filepaths:
    i = int(path.split("_")[-1].replace(".json", ""))
    with open(path) as fp:
        update = json.load(fp)
    with open(path.replace("update_", "update_metadata_")) as fp:
        metadata = json.load(fp)
    
    # plot the level
    matplotlib.rcParams['axes.linewidth'] = 1 #set the value globally
    _, ax = plt.subplots(1, 1, figsize=(5,5))
    level = metadata["associated_controller"]
    wins = metadata["metadata"]["wins"]
    winratio = sum(wins)/len(wins)
    # plot_level_from_array(ax, level, title=r"$w=$" + f" {winratio}")
    plot_level_from_array(ax, level)
    # plt.show()
    # plt.close()
    plt.savefig(f"./zelda_experiments/final_plots/update_viz/level_it_{i}.jpg", dpi=150, bbox_inches="tight")


    # plot the new winrate surface for all partitions, labeling the point that was used (?)
    matplotlib.rcParams['axes.linewidth'] = 5 #set the value globally
    for partition in [partition_1, partition_2, partition_3]:
        keys = list(partition.keys())
        keys.sort()
        centroid_tested = metadata["centroid_tested"]
        centroid_in_plot = [centroid_tested[all_keys.index(keys[0])], centroid_tested[all_keys.index(keys[1])]]
        print(f"TESTED CENTROID {centroid_in_plot}")
        _, ax = plt.subplots(1, 1, figsize=(5,5))
        if i == 0:
            # ax.set_title(r"Performance $p(w)$")
            plot_mean_performance(ax, update, partition, size=250, plot_labels=False, plot_colorbar=False)
        else:
            plot_mean_performance(ax, update, partition, size=250, plot_labels=False, plot_colorbar=False)
        ax.tick_params(
            top=False,
            bottom=False,
            labelbottom=False,
            right=False,
            left=False,
            labelleft=False,
        )
        # ax.plot(centroid_in_plot[:1], centroid_in_plot[1:], "ok")
        plt.savefig(f"./zelda_experiments/final_plots/update_viz/{keys[0]}_{keys[1]}_{i}.jpg", dpi=150, bbox_inches="tight")
    
# Plotting one with colorbar, for the colorbar.
matplotlib.rcParams['axes.linewidth'] = 1 #set the value globally
matplotlib.rc("font", size=26)
_, ax = plt.subplots(1, 1, figsize=(5, 5))
plot_mean_performance(ax, update, partition, size=250, plot_colorbar=True)
# plt.colorbar(scatter, ticks=[0, 0.5, 1])
plt.savefig(f"./zelda_experiments/final_plots/update_viz/colorbar.jpg", dpi=150)


with open(original_gen_path) as fp:
    generation = json.load(fp)

matplotlib.rcParams['axes.linewidth'] = 5
for partition in partitions:
    keys = list(partition.keys())
    keys.sort()
    _, ax = plt.subplots(1, 1, figsize=(5,5))
    plot_mean_performance(ax, generation, partition, size=250, plot_colorbar=False)
    ax.tick_params(
        top=False,
        bottom=False,
        labelbottom=False,
        right=False,
        left=False,
        labelleft=False,
    )
    plt.savefig(f"./zelda_experiments/final_plots/update_viz/{keys[0]}_{keys[1]}_original.jpg", dpi=150, bbox_inches="tight")
