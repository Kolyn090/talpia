import numpy as np
from PIL import Image
from save_img import save_arr_as_png


def create_bg(length, times2, gray1, gray2):
    def resize_array(array):
        return array.repeat(2, axis=0).repeat(2, axis=1)

    arr = np.zeros([length, length, 3], dtype=np.uint8)

    for row in range(length):
        for col in range(length):
            if ((row % 2 == 0 and col % 2 == 0) or
                    (row % 2 == 1 and col % 2 == 1)):
                arr[row, col] = gray1
            else:
                arr[row, col] = gray2

    for _ in range(times2):
        arr = resize_array(arr)

    save_arr_as_png(arr, "bg.png")


create_bg(4, 4, [135, 135, 135], [186, 186, 186])
