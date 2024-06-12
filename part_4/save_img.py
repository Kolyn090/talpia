import numpy as np
from PIL import Image


def save_arr_as_png(arr, filename):
    modified_arr = np.rot90(arr, k=1)
    modified_arr = np.flip(modified_arr, axis=0)
    image = Image.fromarray(modified_arr)
    image.save(f"{filename}.png")
