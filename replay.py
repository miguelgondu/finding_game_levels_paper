import click
import glob
import matplotlib.pyplot as plt
import gym
import gym_gvgai
from shutil import copyfile
from gym.envs.registration import registry, register, make, spec
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

@click.command()
@click.option("--experiment_id", type=str, required=True)
@click.option("--seed", type=int, default=None)
def replay(experiment_id, seed):
    if seed is None:
        playtrace_paths = list(glob.glob(f"./zelda_experiments/playtraces/{experiment_id}_*.txt"))
        playtrace_path = random.choice(playtrace_paths)
    else:
        try:
            playtrace_path = glob.glob(f"./zelda_experiments/playtraces/{experiment_id}_*_{seed}.txt")[0]
        except Exception as e:
            print(e)
            print("Perhaps couldn't find the playtrace file with given experiment_id and seed.")
            return
    level_path = glob.glob(f"./zelda_experiments/levels/{experiment_id}_*.txt")[0]
    
    print("Reading playtrace:")
    print(playtrace_path)
    print("Reading level:")
    print(level_path)

    # Register the level using gym with the appropiate seed
    with open(playtrace_path) as fp:
        playtrace = fp.readlines()
    seed, result, score, steps = playtrace.pop(0).split(" ")
    print(seed, result, score, steps)
    
    ## Registering the level
    copyfile(
        level_path,
        "/Users/migd/Projects/GVGAI_GYM-master/gym_gvgai/envs/games/zelda_v1/zelda_lvl4.txt"
    )
    env_id = f'gvgai-zelda-lvl4-v1'
    if env_id in gym.envs.registry.env_specs:
        del gym.envs.registry.env_specs[env_id]

    register(
        id=env_id,
        entry_point='gym_gvgai.envs.gvgai_env:GVGAI_Env',
        kwargs={'game': "zelda", 'level': 4, 'version': 1, "random_seed": seed},
        max_episode_steps=2000
        #nondeterministic=nondeterministic,
        #Play with different setups here
    )
    
    ## building the environment
    env = gym.make(env_id)
    env.reset()
    actions = env.unwrapped.get_action_meanings()
    # play said playtrace and show the video.
    for i, line in enumerate(playtrace):
        show_state(env, step=i)
        action = line.replace("\n", "")
        action_id = actions.index(action)
        _, _, done, _ = env.step(action_id)
        if done:
            break

if __name__ == "__main__":
    replay()