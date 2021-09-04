import json
import matplotlib.pyplot as plt
import glob
import os

from visualization_utils import plot_level_from_array, plot_mean_winrate, plot_mean_performance

partition_3 = {
    "space coverage": [0.3, 1],
    "reachability": [3.5, 16.5]
}

partition_2 = {
    "leniency": [-0.5, 11.5],
    "reachability": [3.5, 16.5]
}

partition_1 = {
    "space coverage": [0.3, 1],
    "leniency": [-0.5, 11.5]
}

path_to_updates = "./zelda_experiments/updates"
priors = os.listdir(path_to_updates)
priors = [prior for prior in priors if prior[0] != "."]
rewrite = True

for prior in priors:
    path_to_prior = f"{path_to_updates}/{prior}"
    agents = os.listdir(path_to_prior)
    agents = [agent for agent in agents if agent[0] != "."]
    for agent in agents:
        # Process, per iteration (getting it automatically without a for)
        path_to_agent = f"{path_to_prior}/{agent}"
        all_updates = glob.glob(f"{path_to_agent}/update_*.json")
        all_updates = [update for update in all_updates if "metadata" not in update]

        # Finding out all unique iterations.
        update_iterations = {}
        for update in all_updates:
            postfix = update.split("_")[-1]
            prefix = update.replace(postfix, "")

            if prefix not in update_iterations:
                update_iterations[prefix] = []
            update_iterations[prefix].append(postfix)

        # for v in update_iterations.values():
        #     v.sort()

        # if len(update_iterations) < 10:
        #     print(len(update_iterations))

        # At this point, all iterations are separated regardless of iteration_%d.
        for prefix, postfixes in update_iterations.items():
            print(prefix)
            print(f"postfixes: {postfixes}")
            # HOTFIX to get interesting ones.
            if len(postfixes) != 3:
                continue
            fig, axes = plt.subplots(4, len(postfixes), figsize=(5*len(postfixes), 4*5))
            print(axes.shape)
            # print(f"For {prefix}:")
            image_name = prefix.split("/")[-1]
            if len(postfixes) == 1:
                to_iterate_0 = [axes[0]]
                to_iterate_1 = [axes[1]]
                to_iterate_2 = [axes[2]]
                to_iterate_3 = [axes[3]]
            else:
                to_iterate_0 = axes[0, :]
                to_iterate_1 = axes[1, :]
                to_iterate_2 = axes[2, :]
                to_iterate_3 = axes[3, :]
            for ax, i in zip(to_iterate_0, range(len(postfixes))):
                file_ = prefix.replace("update_", "update_metadata_") + str(i) + ".json"
                with open(file_) as fp:
                    metadata = json.load(fp)

                level = metadata["associated_controller"]
                recorded_performance = metadata["recorded_performance"]
                # print(f"level at {i}:")
                # print(metadata["associated_controller"])

                wins = metadata["metadata"]["wins"]
                winrate = sum(wins)/len(wins)
                plot_level_from_array(ax, level, title=f"Update: {i}, p: {recorded_performance:1.3f}, w: {winrate}")
            
            iterable = zip(
                to_iterate_1,
                to_iterate_2,
                to_iterate_3,
                range(len(postfixes))
            )
            for ax1, ax2, ax3, i in iterable:
                file_ = prefix + str(i) + ".json"
                with open(file_) as fp:
                    generation = json.load(fp)
                plot_mean_performance(ax1, generation, partition_1, size=50)
                plot_mean_performance(ax2, generation, partition_2, size=50)
                plot_mean_performance(ax3, generation, partition_3, size=50)
                
            fig.suptitle(image_name)
            # plt.show()
            image_path = f"./zelda_experiments/update_viz/{image_name}.jpg"
            if not os.path.exists(image_path) or rewrite:
                plt.savefig(image_path)
            plt.close()
