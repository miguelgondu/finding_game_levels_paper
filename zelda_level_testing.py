"""
This script contains a generic function that takes an agent
and tests the level using it.

What should the agent look like?, should it have a method
that just acts? (See the generic agent in the gvgai package).
"""

import matplotlib.pyplot as plt
from zelda_level_creation import create_level, register_level
from zelda_pcg_utils import print_to_text
from itertools import repeat
import time
import gym
import multiprocessing as mp
import json
import os
import random

def show_state(env, step):
    # plt.figure()
    plt.show()
    plt.imshow(env.render(mode="rgb_array"))
    plt.title(f"step: {step}")
    plt.axis("off")
    plt.draw()
    plt.pause(0.00001)
    plt.close()
    # display.clear_output(wait=True)
    # display.display(plt.gcf())

def plot_level_and_save(env, filename, title=None):
    plt.figure()
    if title:
        plt.title(title)
    plt.imshow(env.render(mode="rgb_array"))
    plt.axis("off")
    plt.savefig(filename)
    plt.close()

def rollout(agent, env_id, results, max_frames, lvl, id_, show):
    """
    This function tests an agent in en environment, maintianing a results
    dict.
    """
    pid = os.getpid()

    # create a doc for saving the info
    temp_results = {
        "scores": [],
        "steps": [],
        "wins": [],
    }

    # Build it and save a snapshot
    env = gym.make(env_id)

    # Running the rollout
    state = env.reset()
    actions = env.unwrapped.get_action_meanings()
    sum_score = 0

    for i in range(max_frames):
        # Visualize the state if the show flag is True.
        if show:
            show_state(env, i)

        # Get the next action
        action_id = agent.act(state, actions)

        # Play it and record results.
        state, reward, is_over, debug = env.step(action_id)
        sum_score += reward
        if is_over:
            # Storing info for this iteration
            temp_results["scores"].append(sum_score)
            temp_results["steps"].append(i)
            if debug["winner"].endswith("WINS"):
                temp_results["wins"].append(True)
            elif debug["winner"].endswith("LOSES"):
                temp_results["wins"].append(False)
            elif debug["winner"] == "NO_WINNER":
                temp_results["wins"].append(False)
            else:
                raise ValueError(f"Unknown state {debug['winner']}, is there something else besides winning or losing?")
            print(f"Game over at tick {i}, result: {temp_results['wins'][-1]}")
            break
    else:
        temp_results["scores"].append(sum_score)
        temp_results["steps"].append(i)
        temp_results["wins"].append(False)

    results[pid] = temp_results
    env.close()

def aggregate_results(pool_results):
    final_results = {"scores": [], "steps": [], "wins": []}
    for results in pool_results.values():
        final_results["scores"] = [*final_results["scores"], *results["scores"]]
        final_results["steps"] = [*final_results["steps"], *results["steps"]]
        final_results["wins"] = [*final_results["wins"], *results["wins"]]

    return final_results

def test_level(agent, level, rollouts=1, max_frames=2000, save_playtraces=False, lvl="1", parallel=True, show=False):
    '''
    This is the function that tests an agent in a level, doing a certain
    amount of rollouts.
    '''
    # create a doc for saving the info
    level_txt = print_to_text(level)
    doc = {
        "level": level_txt,
        "rollouts": rollouts,
        "scores": [],
        "steps": [],
        "wins": [],
    }

    # I should be checking if the level in the address is already this one,
    # and don't overwrite and overwrite. TODO: fix this.
    env_id = register_level(level_txt, lvl)

    timestamp = time.time()
    # THIS IS THE PRIME OPPORTUNITY FOR TRACEABILITY. TODO: Implement better logging.
    id_ = str(timestamp).replace(".", "_")

    # Register the env once for photo taking.
    print("Rendering the enviroment once for plotting.")
    env = gym.make(env_id)
    if not os.path.exists(f"../outputs/levels_rendered/{id_}_level_plot.png"):
        plot_level_and_save(env, f"../outputs/levels_rendered/{id_}_level_plot.png")
    # env.close()

    print(f"Printed level to file ../outputs/levels_rendered/{id_}_level_plot.png")

    # Rolling out
    if parallel:
        with mp.Manager() as manager:
            results = manager.dict()
            with manager.Pool() as pool:
                pool.starmap(rollout, repeat((agent, env_id, results, max_frames, lvl, id_, show), rollouts))

            print(results)
            print(dict(results))
            results = dict(results)
    else:
        for _ in range(rollouts):
            results = {}
            rollout(agent, env_id, results, max_frames, lvl, id_, show)

    final_results = aggregate_results(results)
    doc = {
        **doc,
        **final_results
    }

    # print(doc)

    # Saving doc
    with open(f"../outputs/random_agent_results/{id_}_results.json", "w") as fp:
        json.dump(
            doc,
            fp,
            indent=2,
            separators=[",", ":"]
        )

    return doc

if __name__ == "__main__":
    pass
    # test_level(2, parallel=False, show=True)
