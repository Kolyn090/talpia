import tkinter as tk

base_height = 800
base_width = 600
theme_color = '#383838'
canvas_len = 512
outline_width = 2
grid_len = 32
sqsize = canvas_len / grid_len

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
        self.canvas.itemconfigure(self.id, fill='black')


for row in range(grid_len):
    for col in range(grid_len):
        x0 = row * sqsize+3
        y0 = col * sqsize+3
        rect = OnePixel(canvas, row, col,
                        x0, y0, sqsize, 'gray', outline_width)

window.mainloop()
