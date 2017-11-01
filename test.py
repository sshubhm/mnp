from Tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("1300x700")
canvas = Canvas(root)
canvas.pack()
im = Image.open("New_Image.png")
cropped = im.crop((0, 0, 400, 671))
tk_im = ImageTk.PhotoImage(cropped)
label1 = Label(root, image=tk_im)
label1.image = tk_im
label1.place(x=0,y=0)

cropped1 = im.crop((400, 0, 530,671))
tk_im = ImageTk.PhotoImage(cropped1)
label2 = Label(root, image=tk_im)
label2.image = tk_im
label2.place(x=400, y=0)

cropped2 = im.crop((530, 0, 650,671))
tk_im = ImageTk.PhotoImage(cropped2)
label3 = Label(root, image=tk_im)
label3.image = tk_im
label3.place(x=530, y=0)

cropped3 = im.crop((650, 0, 790,671))
tk_im = ImageTk.PhotoImage(cropped3)
label4 = Label(root, image=tk_im)
label4.image = tk_im
label4.place(x=650, y=0)

cropped4 = im.crop((790, 0, 1300,671))
tk_im = ImageTk.PhotoImage(cropped4)
label5 = Label(root, image=tk_im)
label5.image = tk_im
label5.place(x=790, y=0)

root.mainloop()