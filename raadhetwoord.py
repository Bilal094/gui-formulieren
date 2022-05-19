import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo

root1 = tk.Tk()
root1.geometry('450x350')
root1.title('Raad het woord - Speler 1')
root1.resizable(False,False)
wordEntry = StringVar()

def player2():
    word = wordEntry.get()
    if len(word) > 0 and len(word) < 4:
        showinfo('Fout', 'Jouw woord heeft minder dan 4 letters!')
    elif len(word) > 7:
        showinfo('Fout', 'Jouw woord heeft meer dan 7 letters!')
    elif len(word) == 0:
        showinfo('Fout', 'Vul eerst een woord in')
    else:
        root1.destroy()
        root2 = tk.Tk()
        root2.geometry('550x350')
        root2.title('Raad het woord - Speler 2')
        root2.resizable(False, False)
        


        root2.mainloop()



label1 = Label(text='Type het woord in', font=('Helvetica', 15)).place(x=150,y=75)
label2 = Label(text='Je woord moet 4 tot 7 letters bevatten').place(x=130,y=150)
entry1 = Entry(textvariable=wordEntry).place(x=165,y=120)
button1 = Button(text='Klaar', relief='ridge', font=(14), command=player2).place(x=200,y=200)


root1.mainloop()