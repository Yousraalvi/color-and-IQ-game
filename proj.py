import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 30
def startGame(object): 
      
    if timeleft == 30:
        countdown()
    nextColour()
def nextColour():
    global score 
    global timeleft
    if timeleft > 0:
         e.focus_set()
         if e.get().lower() == colours[1].lower(): 
              
            score += 1
         e.delete(0, tk.END)
         random.shuffle(colours)
         label.config(fg = str(colours[1]), text = str(colours[0]))
         scoreLabel.config(text = "Score: " + str(score))
def countdown(): 
  
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: "
                               + str(timeleft))
        timeLabel.after(1000, countdown)
        if (timeleft == 0):
            messagebox.showinfo("Time Alert", "Time's up ")
you= tk.Tk()
you.title("EYE TEST COLOR GAME")
you.geometry("475x250")
you.configure(bg="#595b83")
head = tk.Label(you, text = "GAME" ,font = ('Helvetica', 13,'bold italic'),bg="#595b83",fg='#f4abc4')
head.pack()
info = tk.Label(you, text = "Type in the colour"
                        "of the words, and not the word text!", 
                                      font = ('Helvetica', 13,'italic'),bg="#595b83",fg='#f4abc4') 
info.pack()
scoreLabel = tk.Label(you, text = "Press enter to start", 
                                      font = ('Helvetica', 12,'italic'),bg="#595b83",fg='#f4abc4') 
scoreLabel.pack()
timeLabel = tk.Label(you, text = "Time left: " +
              str(timeleft), font = ('Helvetica', 12),bg="#595b83",fg='#f4abc4') 
                
timeLabel.pack()
label = tk.Label(you, font = ('Helvetica', 60),bg="#595b83") 
label.pack()
e = tk.Entry(you,width=60,bd=4)
you.bind('<Return>', startGame) 
e.pack()
e.focus_set()
you.mainloop() 
