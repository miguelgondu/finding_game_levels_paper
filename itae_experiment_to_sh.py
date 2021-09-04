"""
This script creates a shell executable with all the
commands needed to run the all-pairs ITAE test.

The parameters will be as follows: 40 rollouts for consistency
and at most 20 updates.
"""

import datetime
import click

# def experiment(path, rollouts, processors, seed, comment, path_to_updates, agent, parallel):

def write_command(prior_file, agent, iterations, rollouts, processors, performance_bound, seed, updates, comment, path_to_updates, parallel):
    prior_agent = prior_file.split("/")[-1].split("_")[1]
    agent_name = agent.split(".")[-2]

    new_comment = comment + '_prior_' + prior_agent + '_to_' + agent_name
    command = "python zelda_itae_experiment.py "
    command += f"{prior_file} "
    command += f"--iterations={iterations} "
    command += f"--rollouts={rollouts} "
    command += f"--processors={processors} "
    command += f"--performance_bound={performance_bound} "
    command += f"--seed={seed} "
    command += f"--updates={updates} "
    command += f"--comment={new_comment} "
    command += f"--path_to_updates={path_to_updates} "
    command += f"--prior_folder={prior_agent}_prior "
    command += f"--agent={agent} "
    if parallel:
        command += "--parallel"
    else:
        command += "--no-parallel"
    return command + f" > log_prior_{prior_agent}_agent_{agent_name}.txt"

@click.command()
@click.option("--iterations", type=int, default=1)
@click.option("--rollouts", type=int, default=5)
@click.option("--processors", type=int, default=10)
@click.option("--performance_bound", type=float, default=0.75)
@click.option("--seed", type=int, default=17)
@click.option("--updates", type=int, default=15)
@click.option("--comment", type=str, default=None)
@click.option("--path_to_updates", type=str, default=".")
@click.option("--parallel/--no-parallel", default=True)
def write_sh(iterations, rollouts, processors, performance_bound, seed, updates, comment, path_to_updates, parallel):
    time = datetime.datetime.now()
    timestamp = time.strftime("%Y_%m_%d_%Hh_%Mm_%Ss")

    kwargs = {
        "iterations": iterations,
        "rollouts": rollouts,
        "processors": processors,
        "performance_bound": performance_bound,
        "seed": seed,
        "updates": updates,
        "comment": f"{timestamp}_" + comment,
        "path_to_updates": path_to_updates,
        "parallel": parallel
    }

    prior_files = {
        "tracks.singlePlayer.advanced.olets.Agent": "./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "tracks.singlePlayer.advanced.sampleMCTS.Agent": "./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "tracks.singlePlayer.advanced.sampleRHEA.Agent": "./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "tracks.singlePlayer.advanced.sampleRS.Agent": "./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "tracks.singlePlayer.simple.greedyTreeSearch.Agent": "./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "tracks.singlePlayer.simple.sampleonesteplookahead.Agent": "./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "tracks.singlePlayer.simple.sampleRandom.Agent": "./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
        "tracks.singlePlayer.simple.doNothing.Agent": "./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json",
    }

    baseline_prior_file ="./zelda_experiments/generations/generation_baselineRandomPrior_00009.json"
    priors = [baseline_prior_file] + list(prior_files.values())
    script = ""
    for prior_file in priors:
        prior_name = prior_file.split("/")[-1].split("_")[1]
        script += "# " + "-"*80 + "\n"
        script += f"# prior: {prior_name}" + "\n"
        for agent in prior_files.keys():
            if "doNothing" in agent:
                continue
            command = write_command(prior_file, agent, **kwargs)
            script += command + "\n"

    with open(f"./to_run_itae_{timestamp}.sh", "w") as fp:
        fp.write(script)
    
if __name__ == "__main__":
    write_sh() # pylint: disable=no-value-for-parameter
