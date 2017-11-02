#class road
import numpy as np
from TrafficLight import *
import time
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
        print('stealth')
        return "white"

class Road:
    def __init__(self,a,b,C):
        self.createLable(a,b,C)
    def createLight(self,a,b,c,d,e,f,g,h,C):
        self.tLight = TrafficLight(a,b,c,d,e,f,g,h,C)
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
    def createLable(self,a,b,C):
        self.a = a
        self.inner = "0"
        if self.a==0:
            self.inner = ""
        self.txt = C.create_text(a, b, text=self.inner)

    def startTimer(self,C,time1):
        # if(self.a == 0):
        #     time1 = -1
        while time1 != -1:
            C.itemconfig(self.txt, text = time1)
            time.sleep(1)
            time1 = time1 - 1

