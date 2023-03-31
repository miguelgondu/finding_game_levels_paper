"""
This script creates a to_run.sh file that contains all the experiments
to run.
"""

import click
import time
import datetime


@click.command()
@click.option("--generations", type=int, default=10)
@click.option("--iterations", type=int, default=100)
@click.option("--initial_iterations", type=int, default=100)
@click.option("--rollouts", type=int, default=20)
@click.option("--seed", type=int, default=17)
@click.option("--processors", type=int, default=10)
def write_sh(generations, iterations, initial_iterations, rollouts, seed, processors):
    time = datetime.datetime.now()
    timestamp = time.strftime("%Y_%m_%d_%Hh")

    agents = [
        "tracks.singlePlayer.advanced.olets.Agent",
        "tracks.singlePlayer.advanced.sampleMCTS.Agent",
        "tracks.singlePlayer.advanced.sampleRHEA.Agent",
        "tracks.singlePlayer.advanced.sampleRS.Agent",
        "tracks.singlePlayer.simple.greedyTreeSearch.Agent",
        "tracks.singlePlayer.simple.sampleonesteplookahead.Agent",
        "tracks.singlePlayer.simple.sampleRandom.Agent",
        "tracks.singlePlayer.simple.doNothing.Agent",
    ]
    script = ""
    for agent in agents:
        command = "python zelda_map_elites_experiment.py "
        command += f"--generations={generations} "
        command += f"--iterations={iterations} "
        command += f"--initial_iterations={initial_iterations} "
        command += f"--rollouts={rollouts} "
        command += f"--agent={agent} "

        comment = agent.split(".")[-2]  # agent name
        comment += f"_{timestamp}"
        comment += f"_{generations}_gens"
        comment += f"_{iterations}_iter"
        comment += f"_{initial_iterations}_init"
        comment += f"_{rollouts}_roll"
        comment += f"_{seed}_seed"

        command += f"--comment={comment} "
        command += f"--seed={seed} "
        command += f"--processors={processors} "
        command += f"--parallel --save-each-gen"
        command += "\n"

        script += command

    with open(f"to_run_{timestamp}.sh", "w") as fp:
        fp.write(script)


if __name__ == "__main__":
    write_sh()
