import numpy as np
from zelda_map_elites_utils import random_variation, random_solution
from visualization_utils import save_level_from_array


for level_id in range(10):
    for _ in range(5):
        try:
            level = random_solution()
            break
        except ValueError:
            pass
    save_level_from_array(level, f"./zelda_experiments/variations_viz/level_{level_id}_original.jpg")
    for var_id in range(10):
        for _ in range(5):
            try:
                level = random_variation(level)
                break
            except ValueError:
                pass
        save_level_from_array(level, f"./zelda_experiments/variations_viz/level_{level_id}_var_{var_id+1}.jpg")
