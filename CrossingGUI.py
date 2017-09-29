#!/usr/bin/python

import Tkinter
top = Tkinter.Tk()
# Code to add widgets will go here...

C = Tkinter.Canvas(top, bg="#b0b0b0", height=600, width=600)

line = C.create_line(250,50,250,250);
line = C.create_line(50,250,250,250);
line = C.create_line(50,350,250,350);
line = C.create_line(250,350,250,550);
line = C.create_line(350,350,350,550);
line = C.create_line(350,350,550,350);
line = C.create_line(350,250,550,250);
line = C.create_line(350,250,350,50);
line = C.create_line(50,300,250,300, dash=(2,4));
line = C.create_line(300,250,300,50, dash=(2,4));
line = C.create_line(350,300,550,300, dash=(2,4));
line = C.create_line(300,350,300,550, dash=(2,4));

oval = C.create_oval(270,290,290,310, fill="red");
oval = C.create_oval(290,270,310,290, fill="red");
oval = C.create_oval(310,290,330,310, fill="red");
oval = C.create_oval(290,310,310,330, fill="green");

C.pack()
top.mainloop()
