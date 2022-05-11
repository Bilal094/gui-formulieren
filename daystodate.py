import tkinter as tk
import datetime
from tkinter import *
from tkinter import ttk

# Main

def calculate():
    pass

# Root configuration

root = tk.Tk()
root.title('Days to date calculator')
root.geometry('650x450')
root.resizable(False, False)

day = IntVar()
month = StringVar()
year = IntVar()

daySelect = ttk.Combobox(root,textvariable=day)
daySelect['state'] = 'readonly'
daySelect['values'] = ()
daySelect.place(x=60,y=200)
label1 = Label(text='-',font=('Helvetica', 18)).place(x=225,y=193)

monthSelect = ttk.Combobox(root,textvariable=month)
monthSelect['state'] = 'readonly'
monthSelect['values'] = ('januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december')
monthSelect.place(x=260,y=200)
label2 = Label(text='-', font=('Helvetica', 18)).place(x=425,y=193)

yearSelect = ttk.Combobox(root, textvariable=year)
yearSelect['state'] = 'readonly'
yearSelect['values'] = ('')
yearSelect.place(x=460,y=200)

datumLabel = Label(text='Datum:', font=('Helvetica', 16)).place(x=290,y=100)
button1 = Button(text='Calculate',font=('Helvetica', 16),command=calculate).place(x=280,y=300)

root.mainloop()