#!/usr/bin/python

import Tkinter

import time

import cv2

from TrafficLight import *

#from main import rLeft, tLeft, rRight, rTop, rBottom, tRight, tBottom, tTop

class Draw:

    def __init__(self,img1,img2,img3,img4,img5):# cv2.imshow("1", img1)

        cv2.imshow("1", img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.top = Tkinter.Tk()
        #self.C = Tkinter.Canvas(self.top, bg="#b0b0b0", height=768, width=1366)
        self.frame = Tkinter.Frame(self.top, width=1366, height=768, background='white')
        self.frame.pack_propagate(0)
        self.frame.pack()
        self.label = Tkinter.Label(self.frame, image=img1)
        self.label.pack()
        #self.label.place(x=0, y=0, relwidth=1, relheight=1)
        #self.C.pack()
        # line = self.C.create_line(250,50,250,250)
        # line = self.C.create_line(50,250,250,250)
        # line = self.C.create_line(50,350,250,350)
        # line = self.C.create_line(250,350,250,550)
        # line = self.C.create_line(350,350,350,550)
        # line = self.C.create_line(350,350,550,350)
        # line = self.C.create_line(350,250,550,250)
        # line = self.C.create_line(350,250,350,50)
        # line = self.C.create_line(50,300,250,300, dash=(2,4))
        # line = self.C.create_line(300,250,300,50, dash=(2,4))
        # line = self.C.create_line(350,300,550,300, dash=(2,4))
        # line = self.C.create_line(300,350,300,550, dash=(2,4))

        # #left
        # rectangle = self.C.create_rectangle(50,270,250,280, width=0, fill=rLeft.getColor())
        # #top
        # rectangle = self.C.create_rectangle(320,50,330,250, width=0, fill=rTop.getColor())
        # #right
        # rectangle = self.C.create_rectangle(350,320,550,330, width=0, fill=rRight.getColor())
        # #bottom
        # rectangle = self.C.create_rectangle(270,350,280,550, width=0, fill=rBottom.getColor())

        # ovalL = self.C.create_oval(270,290,290,310, fill="red")
        # ovalT = self.C.create_oval(290,270,310,290, fill="orange")
        # ovalR = self.C.create_oval(310,290,330,310, fill="red")
        # ovalB = self.C.create_oval(290,310,310,330, fill="green")


        # tLeft = TrafficLight(270,290,290,310, C)
        # tTop = TrafficLight(290,270,310,290, C)
        # tRight = TrafficLight(310, 290, 330, 310, C)
        # tBottom = TrafficLight(290, 310, 310, 330, C)
        # top.after(1000,tLeft.toggle,C)



    def turnOn(self, light):
        self.C.itemconfig(light, fill='green')

    def turnOff(self, light):
        self.C.itemconfig(light, fill='red')

    def quit(self):
        print('closing')
        self.top.destroy()