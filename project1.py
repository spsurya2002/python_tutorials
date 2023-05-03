import random
from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()

rgb = "#ffffff"

root.geometry("550x170")
root.minsize(600, 150)
root.maxsize(600, 150)
root.title("clock")
def time():
    r = random.randint(10, 99)
    g = random.randint(10, 99)
    b = random.randint(10, 99)
    rgb = "#" + str(r) + str(g) + str(b)
    r1 = random.randint(100, 999)
    g1 = random.randint(0, 99)
    b1 = random.randint(0, 99)
    r1g1b1 = "#" + str(r1)[-2:] + str(g1) + str(b1)
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.config(foreground=rgb)
    label.config(background=r1g1b1)
    label.after(1000, time)
label = Label(root, font=("ds-digital", 100), background="#000000", foreground=rgb)
label.pack(anchor="center")







print("kkj")

time()
mainloop()