'''
Obsolete, see process_generations
'''
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from operator import itemgetter

'''
TODO:
- Implement a visualization using GPs
- Implement the keeping of the best performing genotypes, and
  showing them in the plot itself.
- Implement keeping the info and summaries in a folder for each
  planning agent.
'''


def plot_generation(generation, partition, vmin, vmax, summarize="average"):
    '''
    summarize can be "average" or "best performance".
    '''

    partition_items = list(partition.items())
    partition_items.sort(key=itemgetter(0))

    key_x = partition_items[0][0]
    key_y = partition_items[1][0]
    xlims = partition_items[0][1][:2]
    ylims = partition_items[1][1][:2]

    point_winrate = {}
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

            if summarize == "average":
                if point not in point_winrate:
                    point_winrate[point] = []
                
                point_winrate[point].append(winrate)
            elif summarize == "best performance":
                if point not in point_winrate:
                    point_winrate[point] = (winrate, doc["performance"])

                if point_winrate[point][1] < doc["performance"]:
                    point_winrate[point] = (winrate, doc["performance"])
            else:
                raise ValueError(f"Expected summarize to be either 'average' or 'best performance', but received {summarize}")

    # Computing the points and the colors
    points = []
    winrates = []
    performances = []
    for point, winrate in point_winrate.items():
        if summarize == "average":
            points.append(point)
            winrates.append(sum(winrate) / len(winrate))
        elif summarize == "best performance":
            points.append(point)
            winrates.append(winrate[0])
            performances.append(winrate[1])
    
    points = np.array(points)
    winrates = np.array(winrates)

    _, axes = plt.subplots(1, 2, figsize=(20, 10))
    scatter = axes[0].scatter(points[:, 0], points[:, 1], c=winrates, vmin=vmin, vmax=vmax, s=75)
    axes[0].set_xlim(xlims)
    axes[0].set_ylim(ylims)
    plt.colorbar(scatter, ax=axes[0])

    scatter2 = axes[1].scatter(points[:, 0], points[:, 1], c=performances, vmin=vmin, vmax=vmax, s=75)
    axes[1].set_xlim(xlims)
    axes[1].set_ylim(ylims)
    if isinstance(partition_items[0][0], str):
        axes[0].set_xlabel(partition_items[0][0])
        axes[0].set_ylabel(partition_items[1][0])
    plt.colorbar(scatter2, ax=axes[1])
    axes[0].set_title("Winrates")
    axes[1].set_title("Performance metric (60% winrate)")

    # title = get_name_from_path(filepath).replace("_", " ")
    # ax.set_title(title)
    # plt.savefig(filepath.replace(".json", ".jpg"), format="jpg")
    plt.show()
    plt.close()

def main():
    generation_path = "zelda_experiments/generations/generation_03_03_2020_RHEA_10_gen_100_iter_17_seed_00009.json"
    with open(generation_path) as fp:
        generation = json.load(fp)
    
    partition1 = {
        "space coverage": [0.4, 1],
        "inverse reachability": [3, 16]
    }
    plot_generation(generation, partition1, 0, 1, summarize="best performance")

if __name__ == "__main__":
    main()