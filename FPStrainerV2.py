import tkinter as tk
from tkinter import *
from random import *
from tkinter import messagebox

# Variables
score = 0
timer = 20
letters = ['w', 'a', 's', 'd', 'space']
mouse = {'Button-1' : 'Click', 'Double-Button' : 'Double click', 'Triple-Button' : 'Triple click'}

# Root configuration
root = tk.Tk()
root.title("Simple FPS trainer")
root.geometry("1050x650")
root.resizable(False, False)

def scoreAdd(point):
    global score
    if point == 2:
        score += 2
        root.unbind(f'<{letter}>')
        label.destroy()
        scoreDisplay.config(text=f'Score: {score}')
        mainGame()
    else:
        score += 1
        button.unbind(f'<{mouseButton}>')
        button.destroy()
        scoreDisplay.config(text=f'Score: {score}')
        mainGame()

def mainGame():
    global label, button, letter, mouseButton, widgetType
    randomX, randomY, widgetType = randrange(5, 900), randrange(50, 550), randrange(0,2)
    if widgetType == 1:
        letter = choice(letters)
        label = Label(text=f'Press {letter}',font=('Helvetica', 14),relief='ridge')
        label.place(x=randomX,y=randomY)
        root.bind(f'<{letter}>', lambda event: scoreAdd(2))
    elif widgetType == 0:
        mouseButton = choice(list(mouse))
        button = Button(text=mouse[mouseButton],font=('Helvetica', 14))
        button.place(x=randomX,y=randomY)
        button.bind(f'<{mouseButton}>', lambda event: scoreAdd(1))

def startGame():
    startBtn.destroy()
    entryInput = int(entry.get())
    timeRun(entryInput)
    entry.destroy()
    mainGame()

def entryTime(default):
    global entry, timer
    entry = Entry(width=28)
    entry.insert(0,default)
    entry.place(x=450,y=200)

def timeRun(seconds):
    global score, timer, startBtn
    if seconds == 0:
        end = messagebox.askyesno('Game ended', f'You scored {score} points. Do you want to play again?')
        if end == True:
            score = 0
            entryTime(20)
            startBtn = Button(root, text='Press here to start', font=('Helvetica', 14), command= startGame)
            startBtn.place(x=450,y=300)
            if widgetType == 1:
                label.destroy()
            else:
                button.destroy()
        else:
            root.destroy()
    else:
        seconds -= 1
        timer = seconds
        timeDisplay.config(text=f'Time remaining: {seconds}')
        root.after(1000, timeRun, seconds)

# Labels, button and frame and placement
blackFrame = Frame(bg='black')
blackFrame.pack(fill ='x', ipady=20)

scoreDisplay = Label(blackFrame, text=f'Score: {score}',font= ('Helvetica', 15), bg = 'black', fg = 'white')
scoreDisplay.place(x=10,y=5)

timeDisplay = Label(blackFrame, text=f'Time remaining: {timer}',font= ('Helvetica', 15), bg = 'black', fg = 'white')
timeDisplay.place(x=450,y=5)
entryTime(20)
startBtn = Button(root, text='Press here to start', font=('Helvetica', 14), command= startGame)
startBtn.place(x=450,y=300)

root.mainloop()