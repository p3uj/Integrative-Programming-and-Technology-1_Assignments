#import the 'tkinter module
import tkinter

#function declaration
def buttonClick():
    #create a label that will output after button click
    lblClick = tkinter.Label(root, text="Button was clicked")

    #put label into the window
    lblClick.pack()

# Create the root (base) window
root = tkinter.Tk()

#resize window
root.geometry('500x250')

#Create a label widget
lblHello = tkinter.Label(root, text="Hello, world!")

# Put the label into the window
lblHello.pack()

#Create a button widget
btnClick = tkinter.Button(root, text="Exit", command=buttonClick)
btnClick.pack()

# Start the event loop
root.mainloop()