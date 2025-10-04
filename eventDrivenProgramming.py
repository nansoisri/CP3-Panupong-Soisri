from tkinter import *

def leftClick(event):
    print('leftClick')

def rightClick(event):
    print('rightClick')

def doubleClick(event):
    print('doubleClick')

main = Tk()
button = Button(main, text="My Button")
button.pack()
button.bind("<Button-1>", leftClick)
button.bind("<Button-2>", rightClick)
button.bind("<Double-1>", doubleClick)
main.mainloop()