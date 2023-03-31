import glob
import os
from visualization_utils import save_level


def plot_all_levels(max_amount=None):
    all_level_paths = glob.glob("zelda_experiments/levels/*.txt")
    for i, level_path in enumerate(all_level_paths):
        image_path = level_path.replace("levels", "images").replace(".txt", ".jpg")
        if not os.path.exists(image_path):
            save_level(level_path, image_path)

        if max_amount is not None:
            if i == max_amount:
                break


if __name__ == "__main__":
    plot_all_levels(max_amount=300)
