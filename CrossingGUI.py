#!/usr/bin/python

import Tkinter

import time

from TrafficLight import *

#from main import rLeft, tLeft, rRight, rTop, rBottom, tRight, tBottom, tTop

class Draw:
    top = Tkinter.Tk()
    C = Tkinter.Canvas(top, bg="#b0b0b0", height=600, width=600)

    def __init__(self,rLeft,rRight,rTop,rBottom):
        self.top = Tkinter.Tk()
        self.C = Tkinter.Canvas(self.top, bg="#b0b0b0", height=600, width=600)

        line = self.C.create_line(250,50,250,250)
        line = self.C.create_line(50,250,250,250)
        line = self.C.create_line(50,350,250,350)
        line = self.C.create_line(250,350,250,550)
        line = self.C.create_line(350,350,350,550)
        line = self.C.create_line(350,350,550,350)
        line = self.C.create_line(350,250,550,250)
        line = self.C.create_line(350,250,350,50)
        line = self.C.create_line(50,300,250,300, dash=(2,4))
        line = self.C.create_line(300,250,300,50, dash=(2,4))
        line = self.C.create_line(350,300,550,300, dash=(2,4))
        line = self.C.create_line(300,350,300,550, dash=(2,4))

        #left
        rectangle = self.C.create_rectangle(50,270,250,280, width=0, fill=rLeft.getColor())
        #top
        rectangle = self.C.create_rectangle(320,50,330,250, width=0, fill=rTop.getColor())
        #right
        rectangle = self.C.create_rectangle(350,320,550,330, width=0, fill=rRight.getColor())
        #bottom
        rectangle = self.C.create_rectangle(270,350,280,550, width=0, fill=rBottom.getColor())

        # ovalL = self.C.create_oval(270,290,290,310, fill="red")
        # ovalT = self.C.create_oval(290,270,310,290, fill="orange")
        # ovalR = self.C.create_oval(310,290,330,310, fill="red")
        # ovalB = self.C.create_oval(290,310,310,330, fill="green")


        # tLeft = TrafficLight(270,290,290,310, C)
        # tTop = TrafficLight(290,270,310,290, C)
        # tRight = TrafficLight(310, 290, 330, 310, C)
        # tBottom = TrafficLight(290, 310, 310, 330, C)
        # top.after(1000,tLeft.toggle,C)

        self.C.pack()

    def glow(self, tLight, roads):
        for road in roads:
            self.C.itemconfig(road.tLight.oval, fill="red")
        self.C.itemconfig(tLight.oval, fill='green')

    def quit(self):
        print('closing')
        self.top.destroy()