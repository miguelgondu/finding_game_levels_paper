"""
This script will create a json file for each iteration of
each pair (prior, agent).
"""

import glob
import json
import os
import pandas as pd
import numpy as np

path_to_updates = "./zelda_experiments/updates"
priors = os.listdir(path_to_updates)
priors = [prior for prior in priors if prior[0] != "."]

print(priors)
table = {}
performance_table = {}
final_table = {}
for prior in priors:
    table[prior] = {}
    performance_table[prior] = {}
    final_table[prior] = {}
    path_to_prior = f"{path_to_updates}/{prior}"
    agents = os.listdir(path_to_prior)
    agents = [agent for agent in agents if agent[0] != "."]
    for agent in agents:
        table[prior][agent] = []
        performance_table[prior][agent] = []
        final_table[prior][agent] = {
            "updates": [],
            "successful": [],
            "performances": []
        }
        path_to_agent = f"{path_to_prior}/{agent}"
        path_to_agent = f"{path_to_prior}/{agent}"
        all_updates = glob.glob(f"{path_to_agent}/update_*.json")
        all_updates = [update for update in all_updates if "metadata" not in update]
        update_iterations = {}
        for update in all_updates:
            postfix = update.split("_")[-1]
            prefix = update.replace(postfix, "")

            if prefix not in update_iterations:
                update_iterations[prefix] = []
            update_iterations[prefix].append(postfix)

        result = {
            "prior": prior,
            "agent": agent,
            "iterations": {}
        }
        best_level = None
        best_performance = None

        for prefix, postfixes in update_iterations.items():
            # updates = list(glob.glob(f"{path_to_agent}/update_2020_*_iteration_{iteration}_*.json"))
            updates = list(glob.glob(f"{prefix}*.json"))
            print(f"{prefix}: {len(updates)}.")
            iteration_results = {
                "centroids": [],
                "winrates": [],
                "levels": [],
                "performances": [],
                "mean_scores": [],
                "mean_steps": [],
            }
            table[prior][agent].append(len(updates))
            final_table[prior][agent]["updates"].append(len(updates))
            best_performance_in_iteration = None
            
            for update_path in updates:
                update_metadata_path = update_path.replace("update_", "update_metadata_")
                with open(update_metadata_path) as fp:
                    update_metadata = json.load(fp)

                centroid = update_metadata["centroid_tested"]
                level = update_metadata["associated_controller"]
                performance = update_metadata["recorded_performance"]
                performance_table[prior][agent].append(performance)
                wins = update_metadata["metadata"]["wins"]
                scores = update_metadata["metadata"]["scores"]
                steps = update_metadata["metadata"]["steps"]

                winrate = sum(wins)/len(wins)
                mean_score = sum(scores)/len(scores)
                mean_steps = sum(steps)/len(steps)

                iteration_results["centroids"].append(centroid)
                iteration_results["levels"].append(level)
                iteration_results["performances"].append(performance)
                iteration_results["winrates"].append(winrate)
                iteration_results["mean_scores"].append(mean_score)
                iteration_results["mean_steps"].append(mean_steps)

                if not best_performance or best_performance < performance:
                    # Update best performance and level
                    best_performance = performance
                    best_level = level
                
                if not best_performance_in_iteration or best_performance_in_iteration < performance:
                    best_performance_in_iteration = performance

            result["iterations"][prefix] = iteration_results
            final_table[prior][agent]["successful"].append(best_performance_in_iteration >= 0.75)
            final_table[prior][agent]["performances"].append(best_performance_in_iteration)
        result["best_performance"] = best_performance
        result["best_level"] = best_level

        with open(f"./zelda_experiments/postprocessed_updates/using_{prior}_agent_{agent}.json", "w") as fp:
            json.dump(result, fp)

print(table)

with open("./zelda_experiments/final_tables/update_iterations.json", "w") as fp:
    json.dump(table, fp)

with open("./zelda_experiments/final_tables/final_table.json", "w") as fp:
    json.dump(final_table, fp)

# Saving the table with mean iterations for the article

priors = {
    "olets_prior": "OLETS",
    "sampleMCTS_prior": "MCTS",
    "sampleRHEA_prior": "RHEA",
    "sampleRS_prior": "RS",
    "greedyTreeSearch_prior": "GTS",
    "sampleonesteplookahead_prior": "OSLA",
    "sampleRandom_prior": "Random",
    "doNothing_prior": "doNothing",
    "baselineRandomPrior_prior": "Baseline (noise)"
}

inv_priors = {v: k for k,v in priors.items()}

agents = {
    k.replace("_prior", ""): v for k,v in priors.items() if "baseline" not in k and "doNothing" not in k
}
inv_agents = {v: k for k, v in agents.items()}

df = pd.DataFrame(index=priors.values(), columns=agents.values())
for prior, values in final_table.items():
    new_row = {}
    for agent, agent_name in agents.items():
        if agent not in values:
            print(f"{agent} is not in {values.keys()}")
        updates = np.array(values[agent]["updates"])
        successful = values[agent]["successful"]
        performances = values[agent]["performances"]
        print("-"*80)
        print(f"Prior: {prior}")
        print(f"Agent: {agent}")
        print(f"updates: {updates}")
        print(f"successful: {successful}")
        print(f"performances: {performances}")
        if not any(successful):
            new_row[agent_name] = "\phantom{00.0 }" + f"(0/{len(updates)})"
        else:
            filtered_updates = updates[successful]
            print(f"filtered updates: {filtered_updates}")
            new_row[agent_name] = f"{np.mean(filtered_updates):.1f} ({len(filtered_updates)}/{len(updates)})"
    df.loc[priors[prior]] = new_row
df.index.name = "Prior\\Agent"
print(df)
with open("./zelda_experiments/final_tables/mean_update_iterations_final.csv", "w") as fp:
    fp.write(df.to_csv())
with open("./zelda_experiments/final_tables/mean_update_iterations_final_tex.txt", "w") as fp:
    fp.write(df.to_latex())


df = pd.DataFrame(index=priors.values(), columns=agents.values())
for prior, values in table.items():
    new_row = {}
    for agent, agent_name in agents.items():
        if agent not in values:
            print(f"{agent} is not in {values.keys()}")
        mean_updates = sum(values[agent])/len(values[agent])
        new_row[agent_name] = mean_updates
    df.loc[priors[prior]] = new_row
df.index.name = "Prior\\Agent"
print(df)
with open("./zelda_experiments/final_tables/mean_update_iterations.csv", "w") as fp:
    fp.write(df.to_csv())
with open("./zelda_experiments/final_tables/mean_update_iterations_tex.txt", "w") as fp:
    fp.write(df.to_latex(float_format=lambda x: f"{x:.2f}"))

df_variance = pd.DataFrame(index=priors.values(), columns=agents.values())
for prior, values in table.items():
    new_row = {}
    for agent, agent_name in agents.items():
        if agent not in values:
            print(f"{agent} is not in {values.keys()}")
        mean_variance = np.std(values[agent]) ** 2
        new_row[agent_name] = mean_variance
    df_variance.loc[priors[prior]] = new_row
df_variance.index.name = "Prior\\Agent"
print(df_variance)
with open("./zelda_experiments/final_tables/variance_update_iterations.csv", "w") as fp:
    fp.write(df_variance.to_csv())
with open("./zelda_experiments/final_tables/variance_update_iterations_tex.txt", "w") as fp:
    fp.write(df_variance.to_latex(float_format=lambda x: f"{x:.2f}"))

# # Saving the tables with performances 

df_perf = pd.DataFrame(index=priors.values(), columns=agents.values())
df_perf_var = pd.DataFrame(index=priors.values(), columns=agents.values())
for prior, values in performance_table.items():
    new_row_perf = {}
    new_row_var = {}
    for agent, agent_name in agents.items():
        if agent not in values:
            print(f"{agent} is not in {values.keys()}")
        new_row_perf[agent_name] = np.mean(values[agent])
        new_row_var[agent_name] = np.std(values[agent]) ** 2
    df_perf.loc[priors[prior]] = new_row_perf
    df_perf_var.loc[priors[prior]] = new_row_var

df_perf.index.name = "Prior\\Agent"
df_perf_var.index.name = "Prior\\Agent"
print(df_perf)
print(df_perf_var)
with open("./zelda_experiments/final_tables/mean_update_performances.csv", "w") as fp:
    fp.write(df_perf.to_csv())
with open("./zelda_experiments/final_tables/mean_update_performances_tex.txt", "w") as fp:
    fp.write(df_perf.to_latex(float_format=lambda x: f"{x:.2f}"))
with open("./zelda_experiments/final_tables/variance_update_performances.csv", "w") as fp:
    fp.write(df_perf_var.to_csv())
with open("./zelda_experiments/final_tables/variance_update_performances_tex.txt", "w") as fp:
    fp.write(df_perf_var.to_latex(float_format=lambda x: f"{x:.2f}"))

# # Saving the table with deviations of performances 

# keys = list(table.keys())
# df_perf_var = pd.DataFrame(index=keys, columns=[k.replace("_prior", "") for k in keys])
# for prior, values in performance_table.items():
#     new_row = []
#     for k in keys:
#         # if k == prior:
#         #     new_row.append(0)
#         # else:
#         agent = k.replace("_prior", "")
#         # Compute the mean amount of values[agent]
#         try:
#             new_row.append(np.std(values[agent]))
#         except KeyError:
#             new_row.append(np.NaN)
#     df_perf_var.loc[prior] = new_row

# print(df_perf_var)
# with open("./zelda_experiments/final_tables/variance_update_performances.csv", "w") as fp:
#     fp.write(df_perf_var.to_csv())
