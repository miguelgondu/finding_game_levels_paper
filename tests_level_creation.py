import numpy as np
from zelda_pcg_utils import add_enemies, remove_enemies
from zelda_pcg_utils import add_walls, remove_walls
from zelda_pcg_utils import shrink, expand
from zelda_pcg_utils import a_star_path, get_placeable_positions_inc_path
from zelda_pcg_utils import ENEMY, WALL, AVATAR, KEY, GOAL

from zelda_map_elites_utils import random_solution, random_variation

print("-"*80)
print("Creating a random level")
x = random_solution()
level = np.array(x)
print(level)

print("-"*80)
print("Expanding its height")

level = expand(level, axis=0)
print(level)

print("-"*80)
print("Expanding its width")
level = expand(level, axis=1)
print(level)

print("-"*80)
print("Placeable positions")
print(get_placeable_positions_inc_path(level)) # Seems to be working fine

print("-"*80)
print("Shrinking its height")

level = shrink(level, axis=0)
print(level)

print("-"*80)
print("Shrinking its width")
level = shrink(level, axis=1)
print(level)

print("-"*80)
print("Adding 2 enemies")
add_enemies(level, 2)
print(level)

print("-"*80)
print("Removing one enemy")
remove_enemies(level, 1)
print(level)

print("-"*80)
print("Adding as many walls as possible")
add_walls(level, np.inf)
print(level)

print("-"*80)
print("Removing all inner walls")
remove_walls(level, np.inf)
print(level)

while True:
    print("-"*80)
    print(random_solution())

# x = random_solution()
# level = np.array(x)
# while True:
#     print("-"*80)
#     level = np.array(random_variation(level.tolist()))
#     print(level)

# level_with_no_rem_cols = np.array([
#     ['w', 'w', 'w'],
#     ['w', 'A', 'w'],
#     ['w', '+', 'w'],
#     ['w', 'g', 'w'],
#     ['w', '.', 'w'],
#     ['w', '.', 'w'],
#     ['w', 'w', 'w'],
# ])
# shrink(level_with_no_rem_cols, axis=1)
# shrink(level_with_no_rem_cols.T, axis=0)




# print("-"*80)
# print("Adding an enemy at random")
# add_prompt_at_random(level, ENEMY)
# print(level)

# print("-"*80)
# print("Removing an enemy at random")
# remove_prompt_at_random(level, ENEMY)
# print(level)

# print("-"*80)
# print("Adding a wall at random")
# add_prompt_at_random(level, WALL)
# print(level)

# print("-"*80)
# print("Removing a wall at random")
# remove_prompt_at_random(level, WALL)
# print(level)

# print("-"*80)
# print("Doing a random variation on the level")
# x = random_variation(level.tolist())
# print(np.array(x))

# print("-"*80)
# print("Finding the A* path from player to key.")
# path = a_star_path(level, AVATAR, KEY)
# print(path)
