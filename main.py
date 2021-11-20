# importing libraries
from tkinter import *
from tkinter.ttk import *

from time import strftime

# Creating the window
root = Tk()
root.title("Clock")

def time():
    st = strftime('%H:%M:%S %p')
    label.config(text = st)
    label.after(1000,time)
#Crating a label for the window
label = Label(root, font = ("arial",80),background = "black", foreground = "cyan")
#Packing the label in the window
label.pack(anchor='center')
time()

mainloop()