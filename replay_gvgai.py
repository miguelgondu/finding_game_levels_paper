"""
This script runs a visualization using gvgai's visualization
tools. They don't work very nicely though.
"""
import click
import glob
import os
import random
import subprocess

@click.command()
@click.option("--experiment_id", type=str, required=True)
@click.option("--seed", type=int, default=None)
def play_replay(experiment_id, seed):

    # Get the full paths of the stuff: 0 VGDL 1 level_txt 2 replay file.
    vgdl_path = "/Users/migd/Projects/ITAE_First_Test_paper/code/2020_02_26_experiments/zelda/zelda_experiments/zelda_vgld_desc.txt"
    level_path = glob.glob(f"/Users/migd/Projects/ITAE_First_Test_paper/code/2020_02_26_experiments/zelda/zelda_experiments/levels/{experiment_id}_*.txt")
    assert len(level_path) == 1
    level_path = level_path[0]

    if seed is None:
        playtrace_paths = list(glob.glob(f"/Users/migd/Projects/ITAE_First_Test_paper/code/2020_02_26_experiments/zelda/zelda_experiments/playtraces/{experiment_id}_*.txt"))
        playtrace_path = random.choice(playtrace_paths)
    else:
        try:
            playtrace_path = glob.glob(f"/Users/migd/Projects/ITAE_First_Test_paper/code/2020_02_26_experiments/zelda/zelda_experiments/playtraces/{experiment_id}_*_{seed}.txt")
            assert len(playtrace_path) == 1
            playtrace_path = playtrace_path[0]
        except Exception as e:
            print(e)
            print("Perhaps couldn't find the playtrace file with given experiment_id and seed.")
            return

    # Go to the compiled gvgai folder
    dir_to_gvgai = "/Users/migd/Projects/GVGAI/clients/GVGAI-JavaClient/src/compiled_gvgai"
    os.chdir(dir_to_gvgai)

    # Print the first line to get some context
    with open(playtrace_path) as fp:
        first_line = fp.readline()
    print(first_line)

    # run the command in a subprocess I guess.
    java = subprocess.Popen([
            "java",
            "tracks.singlePlayer.Replay",
            vgdl_path,
            level_path,
            playtrace_path,
        ], stdout=subprocess.PIPE)

if __name__ == "__main__":
    play_replay()
