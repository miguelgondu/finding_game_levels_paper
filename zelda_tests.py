from zelda_map_elites_utils import random_solution, simulate_functional

x = random_solution()
agent = "tracks.singlePlayer.simple.sampleRandom.Agent"

simulate = simulate_functional(agent, 1, parallel=True, rollouts=3)

t = simulate(x)
print(t)