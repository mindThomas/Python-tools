# -*- coding: utf-8 -*-
"""
TIPE:
    - Truc Incroyable Provenant d'Erik
Created on Thu Apr 26 08:53:46 2018
@author: Erik Helmers
"""

import tkinter as tk
import matplotlib as mpl
import matplotlib.animation as animation

# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvasTkAgg  # for Linux?
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvasTk
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class Animation:

    def __init__(self, fig, ax, stream):
        self.stream = stream
        x, y, z = next(stream)
        self.graph = ax.scatter(x, y, z)
        self.graph2 = ax.plot(x, y, z)

        self.previous = []

        self.ani = animation.FuncAnimation(fig, self.update_graph,
                                           interval=10, blit=False)

    def update_graph(self, num):
        self.graph._offsets3d = next(self.stream)
        x, y, z = self.stream.get_backup()
        self.graph2[0].set_data(x, y)
        self.graph2[0].set_3d_properties(z)

    def setTimeStep(self, x):
        self.ani.event_source.interval = x


class Stream:

    def __init__(self, calculFunc):
        self.status = 0
        self.i = 0
        self.step = 1
        self.backup = (np.empty(10000), np.empty(10000), np.empty(10000))
        self.calculFunc = calculFunc
        self.lines = False

    def __next__(self):

        x, y, z = np.empty(1), np.empty(1), np.empty(1)
        x[0], y[0], z[0] = self.calculFunc(self.status)

        if (not self.lines):
            self.i = 0

        self.backup[0][self.i] = x[0]
        self.backup[1][self.i] = y[0]
        self.backup[2][self.i] = z[0]

        self.status += self.step
        self.i += 1
        return x, y, z

    def set_show_lines(self):
        self.lines = not self.lines

    def get_backup(self):
        if self.lines:
            return self.backup[0][:self.i], self.backup[1][:self.i], self.backup[2][:self.i]
        else:
            return np.empty(0), np.empty(0), np.empty(0)

    def setSpeed(self, x):
        self.step = float(x)


class FigureExplorer(tk.Frame):

    def __init__(self, parent, stream):
        tk.Frame.__init__(self, parent)

        figure = Figure(figsize=(5, 5), dpi=100)
        ax = figure.add_subplot(111, projection='3d')
        ax.set_xlim([-5000, 5000])
        ax.set_ylim([-5000, 5000])
        ax.set_zlim([-5000, 5000])

        self.figure = figure
        self.ax = ax

        canvas = FigureCanvasTk(figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)  # Pack

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # 3D HACK
        ax.mouse_init()
        # Parameters
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        self.ani = Animation(figure, ax, stream)


def create_static(method, obj, *args, **kwargs):
    def static(*args, **kwargs):
        print(*args, kwargs)
        return method(*args, **kwargs)

    return static


class Main(tk.Frame):

    def __init__(self, parent, calculusFunc, loadedValues, speed=0.5):
        tk.Frame.__init__(self, parent)
        self.stream = Stream(calculusFunc)
        self.calculusFunc, self.loadedValues = calculusFunc, loadedValues
        self.figure_explorer = FigureExplorer(self, self.stream)
        self.figure_explorer.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.editor_frame = tk.Frame(self, relief=tk.RAISED)
        self.editor_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(self.editor_frame, text="Editor :").pack()

        for name, from_, to, current, setter in [("Speed", 0.01, 5, speed, self.stream.setSpeed)
                                                 ] + self.loadedValues:
            scale = tk.Scale(self.editor_frame, from_=from_, to=to, label=name,
                             orient=tk.HORIZONTAL, resolution=0.01, command=setter)
            scale.set(current)
            scale.pack()
        tk.Checkbutton(self.editor_frame, text="Lines",
                       command=create_static(self.stream.set_show_lines, self.stream)).pack()


def start(clas):
    if not hasattr(clas, "get") or not callable(clas.get):
        raise ValueError("The get(t) function is not defined within " + clas.__name__)

    calculusFunc = clas.get
    loadedValues = []

    for name in filter(lambda x: not x.startswith('__'), dir(clas)):

        if type(getattr(clas, name)) in [float, int]:
            def setter(x):
                setattr(clas, setter.name, float(x))

            setter.name = name
            loadedValues.append((name, -10, 10, getattr(clas, name), setter))
            print("Info : {} was detected to be a {} of value {}".format(name, type(getattr(clas, name)),
                                                                         getattr(clas, name)))

    root = tk.Tk()
    main = Main(root, calculusFunc, loadedValues)
    main.pack(fill=tk.BOTH, expand=True)
    root.mainloop()