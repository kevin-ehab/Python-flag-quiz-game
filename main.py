#Getting the paths to the flags and the names of their countries:
from PIL import Image, ImageTk
import glob
files = glob.glob(r"Flags of the world\*")
countries = [x.replace("Flags of the world\\", "")
             .replace("-", " ")
             .replace(".png", "")
             .replace("flag of ", "")
	         .title() for x in files]

import pandas as pd
series = pd.Series(index = countries, data = files)
#button functions:
import random
def next_round():
    global rounds_number, choice1, choice2, choice3, choice4, correct
    global image_path, bg1 ,bg2 ,bg3 ,bg4, btn1, btn2, btn3, btn4

    rounds_number += 1
    score_label.configure(text=f"score: {score} / {rounds_number}")

    bg1 = bg2 = bg3 = bg4 = "#F0F0F0"

    btn1.configure(bg = bg1, state= "normal")
    btn2.configure(bg = bg2, state= "normal")
    btn3.configure(bg = bg3, state= "normal")
    btn4.configure(bg = bg4, state= "normal")

    

    #reset the countries list:
    countries = list(series.index)

    choice1 = random.choice(countries)
    countries.remove(choice1)

    choice2 = random.choice(countries)
    countries.remove(choice2)

    choice3 = random.choice(countries)
    countries.remove(choice3)

    choice4 = random.choice(countries)
    countries.remove(choice4)

    btn1.configure(text= choice1)
    btn2.configure(text= choice2)
    btn3.configure(text= choice3)
    btn4.configure(text= choice4)

    choices = [choice1, choice2, choice3, choice4]

    correct = random.choice(choices)

    image_path = series[correct]
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)
    flag.configure(image = photo)
    flag.image = photo  # Prevent garbage collection

def button(num):
    global score, bg1 ,bg2 ,bg3 ,bg4 
    if num == 1:
        if choice1 == correct:
            score += 1
            bg1 = "green"
        else:
            bg1 = "red"
    elif num == 2:
        if choice2 == correct:
            score += 1
            bg2 = "green"
        else:
            bg2 = "red"
    elif num == 3:
        if choice3 == correct:
            score += 1
            bg3 = "green"
        else:
            bg3 = "red"
    elif num == 4:
        if choice4 == correct:
            score += 1
            bg4 = "green"
        else:
            bg4 = "red"
    score_label.configure(text=f"score: {score} / {rounds_number}")
    btn1.configure(bg = bg1, state="disabled")
    btn2.configure(bg = bg2, state="disabled")
    btn3.configure(bg = bg3, state="disabled")
    btn4.configure(bg = bg4, state="disabled")

#setting up the game for the first time:
score = 0
rounds_number = 1
bg1 = bg2 = bg3 = bg4 = "#F0F0F0"
choice1 = random.choice(countries)
countries.remove(choice1)
choice2 = random.choice(countries)
countries.remove(choice2)
choice3 = random.choice(countries)
countries.remove(choice3)
choice4 = random.choice(countries)
countries.remove(choice4)
choices = [choice1, choice2, choice3, choice4]
correct = random.choice(choices)
image_path = series[correct]

#interface:
import tkinter as tk

root = tk.Tk()
root.title("Flag game")
root.iconbitmap("icon.ico")
tk.Label(root, width=9).grid(row=0, column=0)
tk.Label(root, width=1).grid(row=0, column=3)

#flag label
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)
flag = tk.Label(root, image=photo)
flag.image = photo  # Prevent garbage collection
flag.grid(row=1, column=1)

#score label
score_label = tk.Label(root, text=f"Score: {score} / {rounds_number}")
score_label.grid(row=0, column=1)

#buttons:

btn1 = tk.Button(root, text= choice1, command= lambda: button(1), bg= bg1)
tk.Label(root, width=5).grid(row=2, column=1)
btn1.grid(row=3, column=1)

btn2 = tk.Button(root, text= choice2, command= lambda: button(2), bg= bg2)
tk.Label(root, width=5).grid(row=4, column=1)
btn2.grid(row=5, column=1)

btn3 = tk.Button(root, text= choice3, command= lambda: button(3), bg= bg3)
tk.Label(root, width=5).grid(row=6, column=1)
btn3.grid(row=7, column=1)

btn4 = tk.Button(root, text= choice4, command= lambda: button(4), bg= bg4)
tk.Label(root, width=5).grid(row=8, column=1)
btn4.grid(row=9, column=1)

new_game_btn = tk.Button(root, text= "Next round", command= next_round, bg= "#6c757d")
tk.Label(root, width=5).grid(row=10, column=1)
new_game_btn.grid(row=11, column=2)
tk.Label(root, width=1).grid(row=12, column=2)


root.mainloop()