import numpy as np
from zelda_map_elites_utils import random_variation, random_solution
from visualization_utils import save_level_from_array

for level_id in range(100):
    for _ in range(5):
        try:
            level = random_solution()
            break
        except ValueError:
            pass
    save_level_from_array(level, f"./zelda_experiments/random_levels_viz/level_{level_id}.jpg")
    