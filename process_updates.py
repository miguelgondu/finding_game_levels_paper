import click
import json
import glob
import numpy as np
from operator import itemgetter
from process_generations import (
    compute_winrate_performance,
    plot_winrate,
    plot_performance,
)
from visualization_utils import plot_mean_performance, plot_mean_winrate
import matplotlib.pyplot as plt


@click.command()
@click.argument("folder_name", type=str)
@click.option("--feat_1", type=str, required=True)
@click.option("--feat_2", type=str, required=True)
@click.option("--max_iterations", type=int, default=None)
def process(folder_name, feat_1, feat_2, max_iterations):
    updates = glob.glob(
        f"./zelda_experiments/updates/{folder_name}/**/update_initial_test_*.json",
        recursive=True,
    )
    all_partitions = {
        "space coverage": [0.3, 1],
        "leniency": [-0.5, 12.5],
        "reachability": [2.5, 16.5],
    }

    partition = {feat_1: all_partitions[feat_1], feat_2: all_partitions[feat_2]}

    for i, update_path in enumerate(updates):
        if max_iterations:
            if i >= max_iterations:
                break
        try:
            with open(update_path) as fp:
                update = json.load(fp)
            _, ax = plt.subplots(1, 1, figsize=(10, 10))
            plot_mean_performance(ax, update, partition)
            plt.savefig(
                update_path.replace(".json", f"_mean_performance_{feat_1}_{feat_2}.jpg")
            )
            plt.close()
        except Exception as e:
            print(f"Couldn't process path {update_path}: {e}")


if __name__ == "__main__":
    process()
