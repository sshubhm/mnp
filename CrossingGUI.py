#!/usr/bin/python

import Tkinter

import time

import cv2

from TrafficLight import *

# from main import rLeft, tLeft, rRight, rTop, rBottom, tRight, tBottom, tTop

from PIL import Image, ImageTk


class Draw:
    def __init__(self, rLeft, rTop, rRight, rBottom):
        self.top = Tkinter.Tk()
        self.C = Tkinter.Canvas(self.top, height=768, width=1366)

        #1st crossing
        line = self.C.create_line(150, 50, 150, 150)
        line = self.C.create_line(50, 150, 150, 150)
        line = self.C.create_line(50, 200, 150, 200)
        line = self.C.create_line(150, 200, 150, 300)
        line = self.C.create_line(200, 200, 200, 300)
        line = self.C.create_line(200, 200, 300, 200)
        line = self.C.create_line(200, 150, 300, 150)
        line = self.C.create_line(200, 150, 200, 50)

        # 2nd T point
        line = self.C.create_line(300, 200, 300, 300)
        line = self.C.create_line(350, 200, 350, 300)
        line = self.C.create_line(350, 200, 450, 200)
        line = self.C.create_line(300, 150, 450, 150)

        #3rd Crossing
        line = self.C.create_line(450, 200, 450, 300)
        line = self.C.create_line(450, 50, 450, 150)
        line = self.C.create_line(500, 200, 500, 300)
        line = self.C.create_line(500, 50, 500, 150)
        line = self.C.create_line(500, 150, 600, 150)
        line = self.C.create_line(500, 200, 600, 200)

        #4th T Point
        line = self.C.create_line(600, 200, 600, 300)
        line = self.C.create_line(650, 200, 650, 300)
        line = self.C.create_line(650, 200, 750, 200)
        line = self.C.create_line(600, 150, 750, 150)

        #5th T point
        line = self.C.create_line(750, 50, 750, 150)
        line = self.C.create_line(800, 50, 800, 150)
        line = self.C.create_line(800, 150, 900, 150)
        line = self.C.create_line(750, 200, 900, 200)

        line = self.C.create_line(50, 175, 150, 175, dash=(2, 4))
        line = self.C.create_line(175, 150, 175, 50, dash=(2, 4))
        line = self.C.create_line(200, 175, 300, 175, dash=(2, 4))
        line = self.C.create_line(175, 200, 175, 300, dash=(2, 4))

        line = self.C.create_line(350, 175, 450, 175, dash=(2, 4))
        line = self.C.create_line(475, 150, 475, 50, dash=(2, 4))
        line = self.C.create_line(500, 175, 600, 175, dash=(2, 4))
        line = self.C.create_line(325, 200, 325, 300, dash=(2, 4))
        line = self.C.create_line(475, 200, 475, 300, dash=(2, 4))
        line = self.C.create_line(625, 200, 625, 300, dash=(2, 4))
        line = self.C.create_line(650, 175, 750, 175, dash=(2, 4))
        line = self.C.create_line(775, 150, 775, 50, dash=(2, 4))
        line = self.C.create_line(800, 175, 900, 175, dash=(2, 4))

        line = self.C.create_line(950,175,975,175,dash=(2,4))
        line = self.C.create_line(970,170,975,175)
        #cd line = self.C.create_line(970,)
        self.C.pack()

        # self.frame = Tkinter.Frame(self.top, width=1366, height=768, background='white')
        # self.frame.pack_propagate(0)
        # self.frame.pack()
        #
        # im = Image.open("New_Image.png")
        # cropped1 = im.crop((0, 0, 430, 671))
        # tk_im1 = ImageTk.PhotoImage(cropped1)
        # self.label1 = Tkinter.Label(self.frame,image=tk_im1)
        # self.label1.image = tk_im1
        # self.label1.place(x=0, y=0)
        # cropped2 = im.crop((430, 0, 530, 671))
        # tk_im2 = ImageTk.PhotoImage(cropped2)
        # self.label2 = Tkinter.Label(self.frame, image=tk_im2)
        # self.label2.image = tk_im2
        # self.label2.place(x=430, y=0)
        # cropped3 = im.crop((530, 0, 650, 671))
        # tk_im3 = ImageTk.PhotoImage(cropped3)
        # self.label3 = Tkinter.Label(self.frame, image=tk_im3)
        # self.label3.image = tk_im3
        # self.label3.place(x=530, y=0)
        # cropped4 = im.crop((650, 0, 790, 671))
        # tk_im4 = ImageTk.PhotoImage(cropped4)
        # self.label4 = Tkinter.Label(self.frame, image=tk_im4)
        # self.label4.image = tk_im4
        # self.label4.place(x=650, y=0)
        # cropped5 = im.crop((790, 0, 1300, 671))
        # tk_im5 = ImageTk.PhotoImage(cropped5)
        # self.label5 = Tkinter.Label(self.frame, image=tk_im5)
        # self.label5.image = tk_im5
        # self.label5.place(x=790, y=0)


        # #left
        # rectangle = self.C.create_rectangle(50,270,150,280, width=0, fill=rLeft.getColor())
        # #top
        # rectangle = self.C.create_rectangle(320,50,330,150, width=0, fill=rTop.getColor())
        # #right
        # rectangle = self.C.create_rectangle(200,320,300,330, width=0, fill=rRight.getColor())
        # #bottom
        # rectangle = self.C.create_rectangle(270,200,280,300, width=0, fill=rBottom.getColor())

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
