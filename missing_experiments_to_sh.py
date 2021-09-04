import json
import os
import glob
import datetime

agents = {
    "olets": "tracks.singlePlayer.advanced.olets.Agent",
    "sampleMCTS": "tracks.singlePlayer.advanced.sampleMCTS.Agent",
    "sampleRHEA": "tracks.singlePlayer.advanced.sampleRHEA.Agent",
    "sampleRS": "tracks.singlePlayer.advanced.sampleRS.Agent",
    "greedyTreeSearch": "tracks.singlePlayer.simple.greedyTreeSearch.Agent",
    "sampleonesteplookahead": "tracks.singlePlayer.simple.sampleonesteplookahead.Agent",
    "sampleRandom": "tracks.singlePlayer.simple.sampleRandom.Agent",
    "doNothing": "tracks.singlePlayer.simple.doNothing.Agent"
}

with open("./zelda_experiments/final_tables/update_iterations.json") as fp:
    update_iterations = json.load(fp)

def write_line(prior_folder, agent, iterations):
    prior_agent = prior_folder.replace("_prior", "")
    prior_file = glob.glob(f"./zelda_experiments/generations/generation_*{prior_agent}*9.json")
    assert len(prior_file) == 1
    prior_file = prior_file[0]

    command = "python zelda_itae_experiment.py "
    command += f"{prior_file} "
    command += f"--iterations={iterations} "
    command += f"--rollouts=40 "
    command += f"--processors=10 "
    command += f"--seed=37 "
    command += f"--updates=20 "
    command += f"--comment=completing_missing_experiments_2020_03_19 "
    command += f"--path_to_updates=./zelda_experiments/updates "
    command += f"--prior_folder={prior_folder} "
    command += f"--agent={agent} "
    command += f"> log_{prior_folder}_to_{agent.split('.')[-2]}.txt "

    return command

script = ""
for prior_folder, updates_per_agent in update_iterations.items():
    script += f"# For {prior_folder}\n"
    print(prior_folder)
    # Write the diagonal
    agent = prior_folder.replace("_prior", "")
    agent = agents[agent]
    script += write_line(prior_folder, agent, 10) + "\n"

    # Write the missing ones
    for agent, updates in updates_per_agent.items():
        if 0 in updates:
            print(f"{agent}: {updates} ({updates.count(0)})")
            agent = agents[agent]
            script += write_line(prior_folder, agent, updates.count(0)) + "\n"

    script += "\n"

print(script)

time = datetime.datetime.now()
timestamp = time.strftime("%Y_%m_%d_%Hh_%Mm_%Ss")
with open(f"to_run_missing_experiments_itae_{timestamp}.sh", "w") as fp:
    fp.write(script)
