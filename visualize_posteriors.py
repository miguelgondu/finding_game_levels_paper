import json
import glob
import matplotlib.pyplot as plt
import numpy as np

from visualization_utils import plot_mean_performance, plot_mean_winrate
from visualization_utils import save_level_from_array

def plot_all_updates(folder_name, agent_name, feat_1, feat_2, pattern="*", comment=None):
    all_partitions = {
        "space coverage": [0.3, 1],
        "leniency": [-0.5, 12.5],
        "reachability": [2.5, 16.5]
    }

    partition = {
        feat_1: all_partitions[feat_1],
        feat_2: all_partitions[feat_2]
    }

    keys = list(all_partitions.keys())
    keys.sort()
    # This will be used for metadata parsing.
    association = {
        key: i for i, key in enumerate(keys)
    }

    keys_partition = list(partition.keys())
    keys_partition.sort()
    
    update_path = glob.glob(f"./zelda_experiments/updates/{folder_name}/{agent_name}/{pattern}_*.json")
    update_path = [path for path in update_path if "metadata" not in path]
    for path in update_path:
        iteration = path.split("/")[-1].split(".")[0].split("_")[-1]
        with open(path) as fp:
            generation = json.load(fp)

        # Plot the mean performance
        _, ax1 = plt.subplots(1, 1, figsize=(10, 10))
        plot_mean_performance(ax1, generation, partition)

        # Plot the dot where the update took place.
        metadata_path = path.replace("update_", "update_metadata_")
        with open(metadata_path) as fp:
            meta = json.load(fp)

        # What a hack, is there a better way of doing this?
        tested_centroid = meta["centroid_tested"]
        proj_point = (
            tested_centroid[
                association[keys_partition[0]]
            ], 
            tested_centroid[
                association[keys_partition[1]]
            ]
        )
        ax1.plot(proj_point[0], proj_point[1], 'ok')


        ax1.set_title(f"Mean performance \n {agent_name} using prior {folder_name}")
        # plt.show()
        path_to_fig = path.replace(f"/updates/{folder_name}/{agent_name}/", "/posteriors/")
        _list = path_to_fig.split("/")

        if comment:
            _list[-1] = f"posterior_{comment}_{feat_1}_{feat_2}_{iteration}.jpg"
        else:
            _list[-1] = f"posterior_{folder_name}_to_{agent_name}_{feat_1}_{feat_2}_{iteration}.jpg"

        path_to_fig = "/".join(_list)
        plt.savefig(path_to_fig, dpi=150)
        plt.close()

        # Saving a snapshot of the level
        level = meta["associated_controller"]
        level_name = _list[-1].replace("posterior_", "level_")
        save_level_from_array(level, f"./zelda_experiments/posterior_levels/{level_name}", title=f"Centroid: {tested_centroid}")


if __name__ == "__main__":
    plot_all_updates("MCTS_prior", "olets", "space coverage", "leniency", pattern="update_presentation")