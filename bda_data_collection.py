"""
Getting the data for the final project of BDA

I'll run 20 rollouts per level, 50 levels, only one agent.
"""
import multiprocessing as mp
import time
import json
import numpy as np
from zelda_map_elites_utils import aggregate_results, run_level, random_solution, print_to_text

def run_one_level(x, agent, n_levels, n_rollouts, original_seed=11, processors=5):
    experiment_id = str(time.time()).replace(".", "_")

    path_to_vgdl = f"/home/mgd/Projects/ITAE_First_Test_paper/code/2020_02_26_experiments/zelda/zelda_experiments/zelda_vgld_desc.txt"

    # save level.
    path_to_level = f"/home/mgd/Projects/bayesian_data_analysis/final_project/raw_data/levels/{experiment_id}.txt"
    print_to_text(x, path_to_level)

    record_path = "None"

    # Compute seeds
    np.random.seed(original_seed)
    seeds = list(range(100))
    np.random.shuffle(seeds)
    seeds = seeds[:n_rollouts]
    np.random.seed()

    with mp.Manager() as manager:
        results = manager.dict()
        arguments = [
            (path_to_vgdl,
            path_to_level,
            agent,
            record_path,
            seed,
            results) for seed in seeds
        ]
        with manager.Pool(processors) as pool:
            pool.starmap(run_level, arguments)
        results = dict(results)
    
    results = aggregate_results(experiment_id, x, agent, "Zelda", original_seed, results)

    important_results = {
        "experiment_id": experiment_id,
        "level": x,
        "wins": results["wins"]
    }

    return important_results

def run_experiment(agent, n_levels, n_rollouts):
    path_to_experiment = "/home/mgd/Projects/bayesian_data_analysis/final_project/raw_data/results"

    for i in range(n_levels):
        print(f"Working on level {i}")
        x = random_solution() # Create a random level
        print(f"Level created:\n {print_to_text(x)}")

        np.random.seed()
        r = run_one_level(x, agent, n_levels, n_rollouts)

        with open(f"{path_to_experiment}/{r['experiment_id']}.json", "w") as fp:
            json.dump(r, fp)

if __name__ == "__main__":
    run_experiment("tracks.singlePlayer.simple.greedyTreeSearch.Agent", 50, 20)
