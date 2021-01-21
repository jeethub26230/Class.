
from tkinter import *
import time

window = Tk()

def a():
    time.sleep(10)
    print('Hello...')


bu = Button(window,text='Click Me',command=a)
bu.pack()

window.mainloop()
