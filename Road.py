#class road
import numpy as np


def color(a):
    if np.array_equal(a, [80, 202, 132]):
        return "green"
    elif np.array_equal(a, [2, 125, 240]):
        return "orange"
    elif np.array_equal(a, [0, 0, 230]):
        return "red"
    elif np.array_equal(a, [19, 19, 158]):
        return "maroon"
    else:
        return a

class Road:
    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

