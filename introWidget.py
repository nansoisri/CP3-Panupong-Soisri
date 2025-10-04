from tkinter import *

def sayHello():
    print('Hello')

mainWindow = Tk()
button = Button(mainWindow, text="Say Hello", command=sayHello,width=20,height=20) .grid(row=4, column=5)
lebel = Label(mainWindow, text="Lecture", width=50, height=5, fg="red", bg="skyblue", font=("Sarabun",36), anchor=W).grid(row=5, column=5)
mainWindow.mainloop()