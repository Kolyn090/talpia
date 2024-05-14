import tkinter as tk
import numpy as np
from vcolorpicker import getColor
from vcolorpicker import rgb2hex
from vcolorpicker import hex2rgb
from PIL import Image

outline_width = 2
base_height = 800
base_width = 600
canvas_len = 512
theme_color = '#383838'
color = '#FFFFFF'
grid_len = 4
arr = np.zeros([grid_len, grid_len, 3], dtype=np.uint8)

window = tk.Tk()
window.resizable(False, False)
window.title('Kolyn Pixel Art Editor')
window.geometry(f"{base_width}x{base_height}")

base = tk.Canvas(window, bg=theme_color)
base.config(width=base_width, height=base_height)
base.pack()

canvas = tk.Canvas(base, bg='white')
canvas.config(width=canvas_len + outline_width, height=canvas_len + outline_width)
canvas.place(x=(base_width - canvas_len) / 2,
             y=(base_height - canvas_len) / 4)


def pick_color():
    global color
    color = f'#{rgb2hex(getColor())}'


button = tk.Button(base,
                   text='pick',
                   command=pick_color)
button.config(width=2, height=1)
button.place(x=300, y=700)


def set_color(*args):
    canvas.itemconfig(args[0], fill='black')


def save_arr_as_png():
    modified_arr = np.rot90(arr, k=1)
    modified_arr = np.flip(modified_arr, axis=0)
    modified_arr = np.uint8(modified_arr)
    image = Image.fromarray(modified_arr)
    image.save("example.png")


button3 = tk.Button(base,
                    text='save',
                    command=save_arr_as_png)
button3.config(width=2, height=1)
button3.place(x=base_width / 2 - 200, y=700)


class OneSquare:
    def __init__(self, can, os_row, os_col, start_x, start_y, size, outline, width):
        self.can = can
        self.id = self.can.create_rectangle((start_x,
                                             start_y,
                                             start_x + size,
                                             start_y + size),
                                            fill="white",
                                            outline=outline,
                                            width=width)
        self.can.tag_bind(self.id, "<ButtonPress-1>", self.set_color)
        self.os_row = os_row
        self.os_col = os_col

    def set_color(self, event=None):
        self.can.itemconfigure(self.id, fill=color)
        m_rgb = hex2rgb(color[1:])
        arr[self.os_row, self.os_col] = [m_rgb[0], m_rgb[1], m_rgb[2]]

    def color_list(self):
        return arr[self.os_row, self.os_col]


# ...
sqsize = canvas_len / grid_len
for row in range(grid_len):
    for col in range(grid_len):
        x0 = row * sqsize + 4
        y0 = col * sqsize + 4
        x1 = (row + 1) * sqsize + 4
        y1 = (col + 1) * sqsize + 4
        pixel = OneSquare(canvas, row, col, x0, y0, sqsize, 'gray', outline_width)
        arr[row, col] = [255, 255, 255]

'''
canvas = tk.Canvas(base, bg='white')
canvas.config(width=canvas_len + GRID_WIDTH, height=canvas_len + GRID_WIDTH)
canvas.place(x=(base_width - canvas_len) / 2,
             y=(base_height - canvas_len) / 8)


def save_arr_as_png():
    m_npa = np.asarray(arr, dtype=np.uint8)
    m_npa = np.rot90(m_npa, k=1)
    m_npa = np.flip(m_npa, axis=0)
    im = Image.fromarray(m_npa)
    im.save("example.png")


def pick_color():
    global color
    color = f'#{rgb2hex(getColor())}'


button3 = tk.Button(base,
                    text='save',
                    command=save_arr_as_png)
button3.config(width=2, height=1)
button3.place(x=base_width / 2 - 200, y=700)

button = tk.Button(base,
                   text='pick',
                   command=pick_color)
button.config(width=2, height=1)
button.place(x=base_width / 2 - 50, y=600)


def print_color():
    print(color)


button2 = tk.Button(base,
                    text='print',
                    command=print_color)
button2.config(width=2, height=1)
button2.place(x=base_width / 2 - 50, y=700)


# https://stackoverflow.com/questions/37060780/changing-rectangle-color-on-click-in-python-using-tk
class OneSquare:
    def __init__(self, can, os_row, os_col, start_x, start_y, size, outline, width):
        self.can = can
        self.id = self.can.create_rectangle((start_x,
                                             start_y,
                                             start_x + size,
                                             start_y + size),
                                            fill="white",
                                            outline=outline,
                                            width=width)
        self.can.tag_bind(self.id, "<ButtonPress-1>", self.set_color)
        self.current_color = '#FFFFFF'
        self.os_row = os_row
        self.os_col = os_col

    def set_color(self, event=None):
        global color
        self.can.itemconfigure(self.id, fill=color)
        m_rgb = hex2rgb(color[1:])
        arr[self.os_row][self.os_col] = [m_rgb[0], m_rgb[1], m_rgb[2]]


sqsize = canvas_len / grid_len

for row in range(grid_len):
    r = []
    for col in range(grid_len):
        x0 = row * sqsize + 3
        y0 = col * sqsize + 3
        rect = OneSquare(canvas, row, col, x0, y0, sqsize, 'gray', GRID_WIDTH)
        rgb = hex2rgb(rect.current_color[1:])
        r.append([rgb[0], rgb[1], rgb[2]])
    npa = np.asarray(r, dtype=np.uint8)
    arr.append(npa)
'''
window.mainloop()