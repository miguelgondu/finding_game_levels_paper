import click
import json
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

def plot_performance(ax, generation, partition, vmin=0, vmax=1):
    '''
    This function plots the winrate in an axis according to a partition.
    '''
    
    # Computing the points and the colors
    points = []
    performances = []
    for doc in generation.values():
        points.append(doc["centroid"])
        performances.append(doc["performance"])
    
    # for point, tuple_ in point_winrate_performance.items():
    #     points.append(point)
    #     performances.append(tuple_[1])

    points = np.array(points)
    performances = np.array(performances)
    keys = list(partition.keys())
    keys.sort()
    ax.set_xlim(partition[keys[0]])
    ax.set_ylim(partition[keys[1]])
    ax.set_zlim(partition[keys[2]])

    ax.set_xlabel(keys[0])
    ax.set_ylabel(keys[1])
    ax.set_zlabel(keys[2])
    scatter = ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=performances, vmin=vmin, vmax=vmax)
    plt.colorbar(scatter, ax=ax)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

partition = {
    "space coverage": [0.3, 1],
    "leniency": [-0.5, 10.5],
    "reachability": [2.5, 16.5]
}

with open("./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json") as fp:
    generation = json.load(fp)

plot_performance(ax, generation, partition)
plt.show()