from tkinter import* 

root = Tk()

def click() :
    label1 = Label(root , text="I was clicked")
    label1.pack()

myButton = Button(root , text="Click me!", command=click)

myButton.pack()

root.mainloop()