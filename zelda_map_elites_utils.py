import numpy as np
import random
import matplotlib.pyplot as plt
import time
import subprocess
import os
import json
import multiprocessing as mp

from zelda_level_testing import test_level
from zelda_pcg_utils import print_to_text, create_random_level
from zelda_pcg_utils import expand, shrink
from zelda_pcg_utils import add_walls, remove_walls
from zelda_pcg_utils import add_enemies, remove_enemies
from zelda_pcg_utils import EMPTY, ENEMY, WALL, AVATAR, GOAL, KEY
from zelda_pcg_utils import ENEMY1, ENEMY2, ENEMY3
from zelda_pcg_utils import a_star_path

# A silly global variable for dealing with paths,
# because I forgot to implement everything properly
# using "import os", lesson learned.

OPERATING_SYSTEM = "Linux"
# OPERATING_SYSTEM = "Mac"

def random_solution():
    """
    This function is supposed to create a random genotype.

    Right now: it's returning as genotype a dict containing
    a summary of the level.

    The future: returning a string of the level. (Or something that's storable
    in jsons, maybe a matrix).
    """

    width = np.random.randint(3, 10)
    height = np.random.randint(3, 10)
    indicator = min(width, height)
    placeable_positions = (width - 2)*(height - 2)

    enemies = np.random.randint(indicator // 2, indicator)
    if indicator > 3:
        walls = np.random.randint(indicator // 2, indicator)
    else:
        walls = 0

    while placeable_positions < 3 + enemies + walls:
        if np.random.randint(0, 11) % 2 == 0:
            width += 1
        else:
            height += 1
        placeable_positions = (width - 2)*(height - 2)

    for i in range(5):
        try:
            level = create_random_level(
                width,
                height,
                0,
                enemies,
                walls
            )
        except ValueError as e:
            specs = (width,height,0,enemies,walls)
            print(f"Couldn't create level with specifications {specs}.")
            print(f"Got exception {e}.")
            print(f"Attempt {i+1}/5.")
            level = None

    if level is None:
        print("Trying again with new random speficifications")
        return random_solution()

    return level.tolist() # Will this work?

def binary_decision():
    nonce = random.random()
    return nonce <= 0.5

def random_variation(x):
    """
    Assuming x is a level.

    We're going to implement the following modifications:
    1. expanding width or height.
    2. adding or removing enemies or walls.
    """

    level = np.array(x)

    decider_height = np.random.randint(0,3)
    decider_width = np.random.randint(0,3)

    if decider_height == 0:
        level = expand(level, axis=0)
    elif decider_height == 1:
        level = shrink(level, axis=0)

    if decider_width == 0:
        level = expand(level, axis=1)
    elif decider_width == 1:
        level = shrink(level, axis=1)
    
    enemy_mod = np.random.randint(-2, 3)
    wall_mod = np.random.randint(-2, 3)

    if enemy_mod > 0:
        add_enemies(level, enemy_mod)
    elif enemy_mod < 0:
        remove_enemies(level, -enemy_mod)

    if wall_mod > 0:
        add_walls(level, wall_mod)
    elif wall_mod < 0:
        remove_walls(level, -wall_mod)

    return level.tolist()

def random_selection(X):
    return random.choice(X)

def compute_performance(results):
    '''
    This function computes the performance based on
    a piece-wise defined function that favors levels
    that make the agents have 0.6 winrate.
    '''
    winratio = sum(results["wins"])/len(results["wins"])
    if winratio <= 0.6:
        return (5/3)*winratio
    else:
        return (-6.25)*winratio**2 + 7.5*winratio - 1.25

def compute_features(results, x):
    '''
    New features:
        - space coverage: opposite of sparseness.
        - inverse leniency: amount of enemies over total.
        - inverse reachability: length of A* paths.
    '''
    features = {}
    level = np.array(x)

    # Feature 1: space coverage.
    level_txt = results["level"]
    total_chars = len(level_txt.replace("\n", ""))
    coverage = (total_chars - level_txt.count(EMPTY)) / total_chars

    features["space coverage"] = coverage

    # Feature 2: inverse leniency.

    total_enemies = level_txt.count(ENEMY1)
    total_enemies += level_txt.count(ENEMY2)
    total_enemies += level_txt.count(ENEMY3)
    features["leniency"] = total_enemies

    # Feature 3: inverse reachability.
    path_to_key = a_star_path(level, root_text=AVATAR, goal_text=KEY)
    path_to_goal = a_star_path(level, root_text=KEY, goal_text=GOAL)
    inv_reachability = len(path_to_key) + len(path_to_goal)
    features["reachability"] = inv_reachability

    return features

def run_level(path_to_vgdl, path_to_level, agent, record_path, seed, results):
    pid = os.getpid()

    # Working from Mac:
    if OPERATING_SYSTEM == "Mac":
        dir_to_gvgai = "/Users/migd/Projects/GVGAI/clients/GVGAI-JavaClient/src/compiled_gvgai"
    elif OPERATING_SYSTEM == "Linux":
        dir_to_gvgai = "/home/mgd/Projects/GVGAI/clients/GVGAI-JavaClient/src/compiled_gvgai"
    
    os.chdir(dir_to_gvgai)
    java = subprocess.Popen([
        "java",
        "tracks.singlePlayer.Simulate",
        path_to_vgdl,
        path_to_level,
        agent,
        record_path.replace(".txt", f"_seed_{seed}.txt"),
        str(seed)
    ], stdout=subprocess.PIPE)
    try:
        results_ = java.stdout.readline().decode("utf8")
        results_ = json.loads(results_)
        results[(pid, seed)] = results_
        java.kill()    
    except json.decoder.JSONDecodeError as e:
        print(f"Couldn't decode the results. {e}")
        java.kill()


def aggregate_results(experiment_id, x, agent, game, original_seed, results):
    agg_results = {
        "experiment_id": experiment_id,
        "agent": agent,
        "game": game,
        "original_seed": original_seed,
        "level": print_to_text(x),
        "seeds": [],
        "scores": [],
        "wins": [],
        "steps": []
    }
    for key, _results in results.items():
        _, seed = key
        agg_results["seeds"].append(seed)
        agg_results["scores"].append(_results["score"])
        agg_results["wins"].append(_results["win"])
        agg_results["steps"].append(_results["steps"])

    return agg_results

def simulate_functional(agent, original_seed, comment="", parallel=True, rollouts=1, processors=None):
    '''
    Returns a function simulate(x) that runs the level x with
    the given agent. For all agents, see the GVGAI implementation
    of Simulate.
    '''
    def simulate(x):
        f''' 
        simulate function that runs level x with the agent
        {agent}
        for {rollouts} times in parallel.
        '''

        '''
        This function should take a level description x in the form of
        a list of lists, write it in the proper place, then call the
        subprocess responsible for running the level {rollouts} amount
        of times in parallel, store the results and compute from that
        the performance (winratio for now) and the behavioral features
        of the level. Performing the behavioral features is agent-
        independent in most cases, so it could be computed apart.
        '''

        # Setting up the timestamp id and all paths.
        experiment_id = str(time.time()).replace(".", "_")
        print(f"Running experiment {experiment_id}")
        if OPERATING_SYSTEM == "Mac":
            prefix = "/Users/migd"
        elif OPERATING_SYSTEM == "Linux":
            prefix = "/home/mgd"

        path_to_vgdl = f"{prefix}/Projects/ITAE_First_Test_paper/code/2020_02_26_experiments/zelda/zelda_experiments/zelda_vgld_desc.txt"
        path_to_level = f"{prefix}/Projects/ITAE_First_Test_paper/code/2020_02_26_experiments/zelda/zelda_experiments/levels/{experiment_id}_{comment}_level.txt"
        record_path = f"{prefix}/Projects/ITAE_First_Test_paper/code/2020_02_26_experiments/zelda/zelda_experiments/playtraces/{experiment_id}_{comment}_playtrace.txt"
        results_path = f"{prefix}/Projects/ITAE_First_Test_paper/code/2020_02_26_experiments/zelda/zelda_experiments/results/{experiment_id}_{comment}_results.json"

        # Writing the level.
        level_text = print_to_text(x, path_to_level)
        print("Running level:")
        print(level_text)

        # Testing the level.
        np.random.seed(original_seed)
        seeds = list(range(100))
        np.random.shuffle(seeds)
        seeds = seeds[:rollouts]
        print(f"Using the following seeds: {seeds}")

        # Refresh the seed for the random variations
        np.random.seed()

        if parallel:
            with mp.Manager() as manager:
                results = manager.dict()
                arguments = [
                    (path_to_vgdl, path_to_level, agent,
                     record_path, seed, results) for seed in seeds
                ]
                with manager.Pool(processors) as pool:
                    pool.starmap(run_level, arguments)
                results = dict(results)
        else:
            results = {}
            for seed in seeds:
                run_level(
                    path_to_vgdl,
                    path_to_level,
                    agent,
                    record_path,
                    seed,
                    results
                )
        
        results = aggregate_results(experiment_id, x, agent, "zelda", original_seed, results)
        # print(results)

        with open(results_path, "w") as fp:
            json.dump(results, fp)

        features = compute_features(results, x) # or path to level? TODO.
        performance = compute_performance(results)

        metadata = {
            "experiment_id": experiment_id,
            "scores": results["scores"],
            "wins": results["wins"],
            "steps": results["steps"]
        }
        return performance, features, metadata

    return simulate
