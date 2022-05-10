import tkinter as tk
import datetime
from tkinter import *
from tkinter import ttk


# months = {'januari' : 31, 'februari' : 28, 'maart' : 31, 'april' : 30, 'mei' : 31, 'juni' : 30 }

root = tk.Tk()
root.geometry('550x450')
root.resizable(False, False)

day = IntVar()
month = StringVar()
year = IntVar()

daySelect = ttk.Combobox(root,textvariable=day)
daySelect['state'] = 'readonly'
daySelect['values'] = ('januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december')
daySelect.grid(column=1,row=3)

root.mainloop()