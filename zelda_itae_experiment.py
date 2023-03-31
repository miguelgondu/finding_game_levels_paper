"""
This script contains the experiment of adapting one agent to another one's map.
"""

import glob
import click
from pyITaE.itae import ITAE
from zelda_map_elites_utils import simulate_functional
import datetime
import os

time = datetime.datetime.now()
timestamp = time.strftime("%Y_%m_%d_%Hh_%Mm_%Ss")


def deploy_functional(agent, seed, comment, parallel, rollouts, processors):
    simulate = simulate_functional(agent, seed, comment, parallel, rollouts, processors)

    def deploy(x):
        performance, behavior, metadata = simulate(x)
        return performance, behavior, metadata

    return deploy


@click.command()
@click.argument("path", type=str)
@click.option("--iterations", type=int, default=1)
@click.option("--rollouts", type=int, default=5)
@click.option("--processors", type=int, default=10)
@click.option("--performance_bound", type=float, default=None)
@click.option("--seed", type=int, default=17)
@click.option("--updates", type=int, default=1000)
@click.option("--comment", type=str, default=None)
@click.option("--path_to_updates", type=str, default=".")
@click.option("--prior_folder", type=str, default=f"itae_updates_{timestamp}")
@click.option("--agent", type=str, default=None)
@click.option("--parallel/--no-parallel", default=True)
def experiment(
    path,
    iterations,
    rollouts,
    processors,
    performance_bound,
    seed,
    updates,
    comment,
    path_to_updates,
    prior_folder,
    agent,
    parallel,
):
    # Make sure that the folders exist
    path_to_prior_folder = f"{path_to_updates}/{prior_folder}"
    if not os.path.exists(path_to_prior_folder):
        os.makedirs(path_to_prior_folder)

    agent_name = agent.split(".")[-2]
    path_to_agent_subfolder = f"{path_to_prior_folder}/{agent_name}"
    if not os.path.exists(path_to_agent_subfolder):
        os.makedirs(path_to_agent_subfolder)

    for iteration in range(iterations):
        deploy = deploy_functional(agent, seed, comment, parallel, rollouts, processors)
        itae = ITAE(
            path,
            deploy,
            comment=f"{comment}_iteration_{iteration}_",
            max_iterations=updates,
            path_to_updates=path_to_agent_subfolder,
            performance_bound=performance_bound,
        )
        itae.run()
        seed += 1


if __name__ == "__main__":
    experiment()  # pylint: disable=no-value-for-parameter
