import random
from tkinter import *

root=Tk()
root.configure(background="#2C3335")
root.title("Dice Roller")
root.geometry("500x400")
# root.maxsize(500,300)
root.wm_iconbitmap(r"C:\Users\deepr\Desktop\GitHub Repos\DiceRoller\icon.ico")
def roll():
    l1.config(text=f"{random.choice(symbols)}")
    l1.pack()

f1=Frame(root,bg='#2C3335')
f1.pack()
symbols=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]

l1=Label(f1,font="Consolas 200",bg='#2C3335', fg='#DAE0E2')
l1.pack(fill=BOTH)
button=Button(f1,text="Roll Dice",font="firacode 16",command=roll)
button.pack()



root.mainloop()
