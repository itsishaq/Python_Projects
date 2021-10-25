#A clock program to setup.

from tkinter import *

from tkinter.ttk import *

from time import strftime

root = Tk()

root.title("CLOCK")

def time():
    str1 = strftime('%H:%M:%S %p')
    
    label.config(text=str1)
    
    label.after(1000,time)

label = Label(root,font=("ds-digital",100),background="red",foreground="black")

label.pack(anchor='center')

time()

mainloop()
