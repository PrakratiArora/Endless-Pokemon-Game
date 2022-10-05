from tkinter import *
import random

root = Tk()

root.title("Esdless pkemon game")
root.geometry("700x500")
root.configure(background = "red")

Player_1 = Label(root,text = "Player 1",bg = "blue",fg = "green")
Player_1.place(relx = 0.1,rely = 0.3,anchor = CENTER)

Player_1_score = Label(root,bg = "blue",fg = "green")
Player_1_score.place(relx = 0.1,rely = 0.5,anchor = CENTER)

Player_2 = Label(root,text = "Player 2",bg = "blue",fg = "green")
Player_2.place(relx = 0.9,rely = 0.3,anchor = CENTER)

Player_2_score = Label(root,bg = "blue",fg = "green")
Player_2_score.place(relx = 0.9,rely = 0.5,anchor = CENTER)

random_dice = Label(root,bg = "blue",fg = "green")
random_dice.place(relx = 0.5,rely = 0.7,anchor = CENTER)

root.mainloop()