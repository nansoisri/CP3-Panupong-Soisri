from tkinter import *

def sayHello():
    print('Hello')

def leftClick(event):
    weight = float(textBoxWeight.get())
    height = float(textBoxHeight.get())
    bmi = round(weight/((height/100)**2),2)
    labelResult.configure(text=str(bmi))
    if bmi < 18.5:
        labelBody.configure(text="ผอมเกินไป")
    elif bmi >= 18.5 and bmi < 25:
        labelBody.configure(text="น้ำหนักปกติ เหมาะสม")
    elif bmi >= 25 and bmi < 30:
        labelBody.configure(text="อ้วน")
    else:
        labelBody.configure(text="อ้วนมาก")



#designGUI
mainWindow = Tk()
labelFrame = Label(mainWindow, text= "BMI", font=("Sarabun")).grid(row=0, column=0)
labelHeight = Label(mainWindow, text= "ส่วนสูง (ซม.)", font=("Sarabun")).grid(row=1, column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=1, column=1)
labelWeight = Label(mainWindow, text= "น้ำหนัก (กก.)", font=("Sarabun")).grid(row=2, column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=2, column=1)
calButton = Button(mainWindow, text="คำนวณ BMI")
calButton.grid(row=3, column=0)
labelResult = Label(mainWindow, text="ผลลัพธ์", font=("Sarabun"))
labelResult.grid(row=3, column=1)
labelBody = Label(mainWindow, text="ดัชนีมวลกาย", font=("Sarabun"), width= 20)
labelBody.grid(row=3, column=2)

calButton.bind("<Button-1>", leftClick)
mainWindow.mainloop()



