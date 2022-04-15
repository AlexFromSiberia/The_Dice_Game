import random
import time
from tkinter import *


def throw():
    x = random.choice(['img\\1.png', 'img\\2.png',
                       'img\\3.png', 'img\\4.png',
                       'img\\5.png', 'img\\6.png'])
    return x


def img(event):
    global b1, b2
    for i in range(5):
        b1 = PhotoImage(file=(throw()))
        b2 = PhotoImage(file=(throw()))
        dice_1['image'] = b1
        dice_2['image'] = b2
        root.update()
        time.sleep(0.15)


root = Tk()
root.geometry('600x300')
root.title("The Dice Game")
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='img\\1.png'))
background = PhotoImage(file='img\\bg.png')
Label(root, image=background).pack()
# Throw txt
throw_txt = Label(root, background='#34a4eb', text='Throw your dices, click on the game board !!!', font=('Comic Sans MS',  20))
throw_txt.place(relx=0.5, rely=0.2, anchor=CENTER)

dice_1 = Label(root)
dice_1.place(relx=0.3, rely=0.6, anchor=CENTER)
dice_2 = Label(root)
dice_2.place(relx=0.7, rely=0.6, anchor=CENTER)
root.bind('<1>', img)
img('event')
root.mainloop()

