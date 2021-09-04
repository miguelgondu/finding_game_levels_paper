'''
This script grabs the last generations and
plots the best performing levels in a similar grid.
'''

import matplotlib.pyplot as plt
import json
import glob
from operator import itemgetter

from visualization_utils import plot_level_from_array

def find_best_k(generation, k):
    all_levels = [
        (
            d["performance"],
            d["solution"],
            sum(d["metadata"]["wins"])/len(d["metadata"]["wins"])
        ) for d in generation.values() if d["solution"] is not None
    ]
    all_levels.sort(key=itemgetter(0), reverse=True)
    return all_levels[:k]



k = 5
generation_paths = glob.glob("./zelda_experiments/generations/*9.json")

for path in generation_paths:
    with open(path) as fp:
        generation = json.load(fp)

    best_k = find_best_k(generation, k)
    fig, axes = plt.subplots(1, k, figsize=(5*k, 5))
    fig.suptitle(path.split("/")[-1].split("_")[1])
    for ax, tuple_ in zip(axes, best_k):
        plot_level_from_array(ax, tuple_[1], title=f"{tuple_[2]}")
    plt.show()

