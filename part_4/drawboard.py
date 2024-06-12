from vcolorpicker import getColor
from vcolorpicker import rgb2hex
from vcolorpicker import hex2rgb
from PIL import Image
import tkinter as tk
import numpy as np

base_height = 800
base_width = 600
theme_color = '#383838'
canvas_len = 512
outline_width = 2
grid_len = 16
sqsize = canvas_len / grid_len
color = '#FFFFFF'
arr = np.zeros([grid_len, grid_len, 3], dtype=np.uint8)


def save_arr_as_png():
    modified_arr = np.rot90(arr, k=1)
    modified_arr = np.flip(modified_arr, axis=0)
    image = Image.fromarray(modified_arr)
    image.save("talpia.png")


window = tk.Tk()
window.resizable(False, False)
window.title('talpia by Kolyn Lin')
window.geometry(f"{base_width}x{base_height}")

base = tk.Canvas(window, bg=theme_color)
base.config(width=base_width, height=base_height)
base.pack()

canvas = tk.Canvas(base, bg='white')
canvas.config(width=canvas_len, height=canvas_len)
canvas.place(x=(base_width - canvas_len) / 2,
             y=(base_height - canvas_len) / 8)

button3 = tk.Button(base,
                    text='save',
                    command=save_arr_as_png)
button3.config(width=2, height=1)
button3.place(x=base_width / 2 - 200, y=700)


def pick_color():
    global color
    color = f'#{rgb2hex(getColor())}'


button = tk.Button(base,
                   text='pick',
                   command=pick_color)
button.config(width=2, height=1)
button.place(x=300, y=700)


class OnePixel:
    def __init__(self, m_canvas, pixel_row, pixel_col,
                 start_x, start_y, size, outline, width):
        self.canvas = m_canvas
        self.id = self.canvas.create_rectangle((start_x,
                                                start_y,
                                                start_x + size,
                                                start_y + size),
                                               fill="white",
                                               outline=outline,
                                               width=width)
        self.canvas.tag_bind(self.id, "<ButtonPress-1>", self.set_color)
        self.row = pixel_row
        self.col = pixel_col

    def set_color(self, event=None):
        self.canvas.itemconfigure(self.id, fill=color)
        m_rgb = hex2rgb(color[1:])
        arr[self.row, self.col] = [m_rgb[0], m_rgb[1], m_rgb[2]]


for row in range(grid_len):
    for col in range(grid_len):
        x0 = row * sqsize + 3
        y0 = col * sqsize + 3
        rect = OnePixel(canvas, row, col,
                        x0, y0, sqsize, 'gray', outline_width)
        arr[row, col] = [255, 255, 255]

window.mainloop()
