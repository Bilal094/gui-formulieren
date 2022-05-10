import tkinter as tk
from tkinter import *

root = tk.Tk()

color = ['black', 'white']
colorIndex = 0
Row = 0
root.resizable(False, False)

def generator(count,rowCount):
    global colorIndex
    label = Label(bg=color[colorIndex])
    label.grid(column=count,row=rowCount, ipadx=50,ipady=50)
    if colorIndex == 0:
        colorIndex = 1
    else:
        colorIndex = 0
    
for x in range(1,6):
    for y in range(5):
        generator(y,Row) 
    Row += 1

root.mainloop()