from tkinter import *

def sayHello():
    print('Hello')

mainWindow = Tk()
button = Button(mainWindow, text="Say Hello", command=sayHello)
button.place(x=50, y=100)
mainWindow.mainloop()

#can use .grid for example: button = Button(mainWindow, text="Say Hello", command=sayHello).grid(row=1,column=1)