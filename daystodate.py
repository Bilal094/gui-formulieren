from time import strftime
import tkinter as tk
import datetime
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

# Main

def dayToMonth(event):
    global month
    month = monthSelect.get()
    if month in month31:
        daySelect['values'] = ([i for i in range(32)])
    if month in month30:
        daySelect['values'] = ([i for i in range(31)])
    if month in month28:
        daySelect['values'] = ([i for i in range(29)])

def calculate():
    day = int(daySelect.get())
    year = int(yearSelect.get())
    if year == int(dateToday.strftime("%Y")) and month == dateToday.strftime("%b") and day == int(dateToday.strftime("%d")):
        showinfo('Days to date calculator', 'Dit is vandaag')
    else:
        pass

# Root configuration
month31 = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
month30 = ['Apr', 'Jun', 'Sept', 'Nov']
month28 = ['Feb']
dateToday = datetime.datetime.now()

root = tk.Tk()
root.title('Days to date calculator')
root.geometry('650x450')
root.resizable(False, False)

day = IntVar()
month = StringVar()
year = IntVar()

daySelect = ttk.Combobox(root,textvariable=day)
daySelect['state'] = 'readonly'
daySelect['values'] = ('31', '30')
daySelect.place(x=60,y=200)
label1 = Label(text='-',font=('Helvetica', 18)).place(x=225,y=193)

monthSelect = ttk.Combobox(root,textvariable=month)
monthSelect['state'] = 'readonly'
monthSelect['values'] = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
monthSelect.place(x=260,y=200)
label2 = Label(text='-', font=('Helvetica', 18)).place(x=425,y=193)
monthSelect.bind('<<ComboboxSelected>>', dayToMonth)

yearSelect = Entry(font=(9))
yearSelect.place(x=460,y=200)

datumLabel = Label(text='Datum:', font=('Helvetica', 16)).place(x=290,y=100)
button1 = Button(text='Calculate',font=('Helvetica', 16),command=calculate).place(x=280,y=300)

root.mainloop()