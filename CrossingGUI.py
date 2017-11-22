#!/usr/bin/python

import Tkinter

import time

import cv2

from TrafficLight import *

# from main import rLeft, tLeft, rRight, rTop, rBottom, tRight, tBottom, tTop

from PIL import Image, ImageTk


class Draw:
    def __init__(self, c1,c2,c3,c4,c5):
        self.top = Tkinter.Tk()
        self.C = Tkinter.Canvas(self.top, height=768, width=1366)

        y=150
        x=0

        #1st crossing
        line = self.C.create_line(150, 50+y, 150, 150+y)
        line = self.C.create_line(50, 150+y, 150, 150+y)
        line = self.C.create_line(50, 250+y, 150, 250+y)
        line = self.C.create_line(150, 250+y, 150, 350+y)
        line = self.C.create_line(250, 250+y, 250, 350+y)
        line = self.C.create_line(250, 250+y, 350, 250+y)
        line = self.C.create_line(250, 150+y, 350, 150+y)
        line = self.C.create_line(250, 150+y, 250, 50+y)

        # 2nd T point
        line = self.C.create_line(350, 250+y, 350, 350+y)
        line = self.C.create_line(450, 250+y, 450, 350+y)
        line = self.C.create_line(450, 250+y, 550, 250+y)
        line = self.C.create_line(350, 150+y, 550, 150+y)

        #3rd Crossing
        line = self.C.create_line(550, 250+y, 550, 350+y)
        line = self.C.create_line(550, 50+y, 550, 150+y)
        line = self.C.create_line(650, 250+y, 650, 350+y)
        line = self.C.create_line(650, 50+y, 650, 150+y)
        line = self.C.create_line(650, 150+y, 750, 150+y)
        line = self.C.create_line(650, 250+y, 750, 250+y)

        #4th T Point
        line = self.C.create_line(750, 250+y, 750, 350+y)
        line = self.C.create_line(850, 250+y, 850, 350+y)
        line = self.C.create_line(850, 250+y, 950, 250+y)
        line = self.C.create_line(750, 150+y, 950, 150+y)

        #5th T point
        line = self.C.create_line(950, 50+y, 950, 150+y)
        line = self.C.create_line(1050, 50+y, 1050, 150+y)
        line = self.C.create_line(1050, 150+y, 1150, 150+y)
        line = self.C.create_line(950, 250+y, 1150, 250+y)

        line = self.C.create_line(50, 200+y, 150, 200+y, dash=(2, 4))
        line = self.C.create_line(200, 150+y, 200, 50+y, dash=(2, 4))
        line = self.C.create_line(250, 200+y, 350, 200+y, dash=(2, 4))
        line = self.C.create_line(200, 250+y, 200, 350+y, dash=(2, 4))

        line = self.C.create_line(450, 200+y, 550, 200+y, dash=(2, 4))
        line = self.C.create_line(600, 150+y, 600, 50+y, dash=(2, 4))
        line = self.C.create_line(650, 200+y, 750, 200+y, dash=(2, 4))
        line = self.C.create_line(400, 250+y, 400, 350+y, dash=(2, 4))
        line = self.C.create_line(600, 250+y, 600, 350+y, dash=(2, 4))
        line = self.C.create_line(800, 250+y, 800, 350+y, dash=(2, 4))
        line = self.C.create_line(850, 200+y, 950, 200+y, dash=(2, 4))
        line = self.C.create_line(1000, 150+y, 1000, 50+y, dash=(2, 4))
        line = self.C.create_line(1050, 200+y, 1150, 200+y, dash=(2, 4))
        line = self.C.create_line(1250, 200+y, 1225, 200+y, dash=(2,4))
        line = self.C.create_line(1240, 190+y, 1250, 200+y)
        line = self.C.create_line(1240, 210+y, 1250, 200+y)

        txt = self.C.create_text(1000, 200+y, text="NSP")
        txt = self.C.create_text(18, 200+y, text="Rohini")
        # txt = self.C.create_text(270, 140, text="Pitampura metro")
        # txt = self.C.create_text(550, 140, text="Pitampura")cd

        # txt = self.C.create_text(145, 143, text="0")
        # txt = self.C.create_text(205, 143, text="1")
        # txt = self.C.create_text(205, 208, text="2")
        # txt = self.C.create_text(145, 208, text="3")
        #
        # txt = self.C.create_text(295, 143, text="0")
        # txt = self.C.create_text(355, 208, text="1")
        # txt = self.C.create_text(295, 208, text="2")
        #
        # txt = self.C.create_text(445, 143, text="0")
        # txt = self.C.create_text(505, 143, text="1")
        # txt = self.C.create_text(505, 208, text="2")
        # txt = self.C.create_text(445, 208, text="3")
        #
        # txt = self.C.create_text(595, 143, text="0")
        # txt = self.C.create_text(655, 208, text="1")
        # txt = self.C.create_text(595, 208, text="2")
        #
        # txt = self.C.create_text(745, 143, text="0")
        # txt = self.C.create_text(805, 143, text="1")
        # txt = self.C.create_text(805, 208, text="2")

        # txt = self.C.create_text(18, 175, text="Rohini")

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
