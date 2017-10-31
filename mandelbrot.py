import time
from tkinter import *
from random import randint
from style import colors
colors = colors()
colors.colorScheme = colors.stripy

def point_in_mandelbrot(x, y):
    z = 0
    c = x + y*1J
    depth = 0
    while depth < 100 and abs(z) < 2:
        z = z**2 + c
        depth += 1
    return depth

class App:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.control = Frame(self.frame)
        self.control.pack(side=TOP)

        label = Label(self.control, text="mandelbrot")
        label.pack(side=LEFT)

        self.width = 640
        self.heigth = 480

        self.canvas = Canvas(self.frame, width=self.width, height=self.heigth)
        self.canvas.pack(side=BOTTOM)

        for x in range(self.width):
            for y in range(self.heigth):
                mandelbrot = point_in_mandelbrot((x-self.width/2)/100, (y-self.heigth/2)/100)
                color = colors.get(mandelbrot, 100)
                self.canvas.create_line(x, y, x + 1, y, fill=color)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
