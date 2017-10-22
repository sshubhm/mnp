#!/usr/bin/python

import Tkinter

from main import rLeft, tLeft, rRight, rTop, rBottom, tRight, tBottom, tTop

top = Tkinter.Tk()
#currently run it as a seperate file  using "python CrossingGUI.py"

C = Tkinter.Canvas(top, bg="#b0b0b0", height=600, width=600)

line = C.create_line(250,50,250,250)
line = C.create_line(50,250,250,250)
line = C.create_line(50,350,250,350)
line = C.create_line(250,350,250,550)
line = C.create_line(350,350,350,550)
line = C.create_line(350,350,550,350)
line = C.create_line(350,250,550,250)
line = C.create_line(350,250,350,50)
line = C.create_line(50,300,250,300, dash=(2,4))
line = C.create_line(300,250,300,50, dash=(2,4))
line = C.create_line(350,300,550,300, dash=(2,4))
line = C.create_line(300,350,300,550, dash=(2,4))

rectangle = C.create_rectangle(50,270,250,280, width=0, fill=rLeft.getColor())
rectangle = C.create_rectangle(350,320,550,330, width=0, fill=rTop.getColor())
rectangle = C.create_rectangle(320,50,330,250, width=0, fill=rRight.getColor())
rectangle = C.create_rectangle(270,350,280,550, width=0, fill=rBottom.getColor())

oval = C.create_oval(270,290,290,310, fill="red")
oval = C.create_oval(290,270,310,290, fill="red")
oval = C.create_oval(310,290,330,310, fill="red")
oval = C.create_oval(290,310,310,330, fill="green")


C.pack()
top.mainloop()

# algo willl be written in this funcition
def updateTrafficLight():
    if(rLeft.getColor() == "green" & rRight.getColor()=="green" & rTop.getColor()=="green" & rBottom.getColor()=="green"):
        tLeft.setTime(10)
        tRight.setTime(10)
        tBottom.setTime(10)
        tTop.setTime(10)
