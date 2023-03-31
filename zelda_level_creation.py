"""
In this script, I plan to write a script that creates and registers
Zelda levels on the GYM GVGAI, to then be called for at testing time.
"""

import time
import numpy as np
import json
import os
import gym

# import gym_gvgai
import matplotlib.pyplot as plt
from zelda_pcg_utils import create_random_level, print_to_text


def create_level(width=None, height=None, loot=None, enemies=None, walls=None):
    """
    This function creates a random level with the specifications above
    and returns the level dict.
    """

    timestamp = time.time()
    seed = int(str(timestamp).replace(".", "")[8:])
    # np.random.seed(seed)

    if width is None:
        width = np.random.randint(3, 10)

    if height is None:
        height = np.random.randint(3, 10)

    indicator = min(width, height)

    if loot is None:
        loot = np.random.randint(indicator // 2, indicator)

    if enemies is None:
        enemies = np.random.randint(indicator // 2, indicator)

    if walls is None:
        if indicator > 3:
            walls = np.random.randint(indicator // 2, indicator)
        else:
            walls = 0

    level = create_random_level(width, height, loot, enemies, walls)

    path = f"../outputs/levels/{str(timestamp).replace('.', '_')}_dungeon_level_random_agent.json"

    level_text = print_to_text(level)
    print(level_text)
    document = {"timestamp": timestamp, "seed": seed, "txt": level_text}

    with open(path, "w") as f:
        json.dump(document, f, separators=[",", ":"], indent=4)

    return document


def register_level(level, game="zelda", lvl="1", path_to_games=None):
    """
    This function registers the level in the gym_gvgai framework, and returns the
    name of the env.
    """

    # Create the folder (?)
    if path_to_games is None:
        path_to_games = "/Users/migd/Projects/GVGAI_GYM-master/gym_gvgai/envs/games"

    # Rewrite whatever is in there (?)
    path_to_game = path_to_games + "/zelda_v1"

    with open(path_to_game + f"/zelda_lvl{lvl}.txt", "w") as fp:
        fp.write(level)

    # Register that level in particular (?)
    env_id = f"gvgai-zelda-lvl{lvl}-v1"
    try:
        gym.register(
            id=env_id,
            entry_point="gym_gvgai.envs.gvgai_env:GVGAI_Env",
            kwargs={
                "game": "zelda",
                "level": int(lvl),
                "version": 1,
            },  #'obs_type': obs_type
            max_episode_steps=2000
            # nondeterministic=nondeterministic,
            # Play with different setups here
        )
    except gym.error.Error:
        print(f"Couldn't register env {env_id}. Was it registered before?")

    return env_id
