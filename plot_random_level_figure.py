import matplotlib.pyplot as plt
from zelda_map_elites_utils import random_solution, random_variation
from visualization_utils import plot_level_from_array, save_level_from_array
import datetime


while True:
    time = datetime.datetime.now()
    timestamp = time.strftime("%Y_%m_%d_%Hh_%Mm_%Ss")
    level = random_solution()

    var1 = random_variation(level)
    var2 = random_variation(level)
    var3 = random_variation(level)

    fig, (ax0, ax1, ax2, ax3) = plt.subplots(1, 4)

    plot_level_from_array(ax0, level, title="Original")
    plot_level_from_array(ax1, var1, title="Variation 1")
    plot_level_from_array(ax2, var2, title="Variation 2")
    plot_level_from_array(ax3, var3, title="Variation 3")

    plt.show()
    flag = input("Save these? (y/[n]): ")
    if flag == "y":
        save_level_from_array(level, f"./zelda_experiments/final_plots/random_variations_viz/original_{timestamp}.jpg", dpi=150)
        save_level_from_array(var1, f"./zelda_experiments/final_plots/random_variations_viz/var1_{timestamp}.jpg", dpi=150)
        save_level_from_array(var2, f"./zelda_experiments/final_plots/random_variations_viz/var2_{timestamp}.jpg",  dpi=150)
        save_level_from_array(var3, f"./zelda_experiments/final_plots/random_variations_viz/var3_{timestamp}.jpg", dpi=150)
    plt.close()