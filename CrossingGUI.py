#!/usr/bin/python

import Tkinter

import time

import cv2

from TrafficLight import *

#from main import rLeft, tLeft, rRight, rTop, rBottom, tRight, tBottom, tTop

from PIL import Image, ImageTk

class Draw:

    def __init__(self,img1,img2,img3,img4,img5):

        self.top = Tkinter.Tk()
        #self.C = Tkinter.Canvas(self.top, height=671, width=1300)
        self.frame = Tkinter.Frame(self.top, width=1366, height=768, background='white')
        self.frame.pack_propagate(0)
        self.frame.pack()

        im = Image.open("New_Image.png")
        cropped1 = im.crop((0, 0, 430, 671))
        tk_im1 = ImageTk.PhotoImage(cropped1)
        self.label1 = Tkinter.Label(self.frame,image=tk_im1)
        self.label1.image = tk_im1
        self.label1.place(x=0, y=0)
        cropped2 = im.crop((430, 0, 530, 671))
        tk_im2 = ImageTk.PhotoImage(cropped2)
        self.label2 = Tkinter.Label(self.frame, image=tk_im2)
        self.label2.image = tk_im2
        self.label2.place(x=430, y=0)
        cropped3 = im.crop((530, 0, 650, 671))
        tk_im3 = ImageTk.PhotoImage(cropped3)
        self.label3 = Tkinter.Label(self.frame, image=tk_im3)
        self.label3.image = tk_im3
        self.label3.place(x=530, y=0)
        cropped4 = im.crop((650, 0, 790, 671))
        tk_im4 = ImageTk.PhotoImage(cropped4)
        self.label4 = Tkinter.Label(self.frame, image=tk_im4)
        self.label4.image = tk_im4
        self.label4.place(x=650, y=0)
        cropped5 = im.crop((790, 0, 1300, 671))
        tk_im5 = ImageTk.PhotoImage(cropped5)
        self.label5 = Tkinter.Label(self.frame, image=tk_im5)
        self.label5.image = tk_im5
        self.label5.place(x=790, y=0)
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