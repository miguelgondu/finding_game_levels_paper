"""
In this script I give MAP-Elites control over level creation
and testing.
"""
import click
from zelda_map_elites_utils import simulate_functional, random_solution
from zelda_map_elites_utils import random_selection, random_variation
from pymelites.map_elites import MAP_Elites

@click.command()
@click.option("--generations", type=int, default=100)
@click.option("--iterations", type=int, default=100)
@click.option("--initial_iterations", type=int, default=100)
@click.option("--rollouts", type=int, default=5)
@click.option("--agent", type=str, default="tracks.singlePlayer.simple.sampleRandom.Agent")
@click.option("--comment", type=str, default="map_elites_experiment")
@click.option("--seed", type=int, default=17)
@click.option("--processors", type=int, default=5)
@click.option("--parallel/--no-parallel", default=True)
@click.option("--save-each-gen/--no-save-each-gen", default=False)
def run_experiment(generations, iterations, initial_iterations, rollouts, agent, comment, seed, processors, parallel, save_each_gen):
    # Get the simulate function for this agent
    simulate = simulate_functional(agent, seed, comment, parallel, rollouts, processors)

    # Create the MAP-Elites object
    map_elites = MAP_Elites(
        random_solution=random_solution,
        random_selection=random_selection,
        random_variation=random_variation,
        simulate=simulate
    )

    partition = {
        "space coverage": [0, 1, 20],
        "leniency": [-0.5, 20.5, 22],
        "reachability": [0.5, 20.5, 21]
    }

    # Create the cells for said MAP-Elites object
    # TODO: should I be exposing this as well?
    map_elites.create_cells(
        partition=partition
    )

    map_elites.compute_archive(
        generations=generations,
        iterations_per_gen=iterations,
        initial_iterations=initial_iterations,
        save_each_gen=save_each_gen,
        comment=comment,
        generation_path="./zelda_experiments/generations"
    )

if __name__ == "__main__":
    run_experiment()