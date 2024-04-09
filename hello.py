from tkinter import* 

# this has to come before anything else in tkinter 
# it creates the windows 
root = Tk()



# everything in tkinter is a widget and its a two step process 
# 1) creating a widget 
# 2) displaying it in the screen

# creating a widget
myLabel = Label(root , text="Hello World!")

# shoving it onto the window screen
myLabel.pack() 
# pack() makes the text stay in the center of the screen

root.mainloop()