#import the 'tkinter module
import tkinter

#function declaration
def buttonClick():
    # Call the get() operation to get the text value
    inputText = txtEntry.get()

    #create a label widget
    lblOutput=tkinter.Label(root, text=inputText)
    lblOutput.pack()

#Create the parent window
root = tkinter.Tk()
root.geometry('500x250')

#Create the button
btnShow = tkinter.Button(root, text="Show Text", command=buttonClick)
btnShow.pack()

#createTextBox(root)
txtEntry = tkinter.Entry(root)
txtEntry.pack()

# Start the event loop
root.mainloop()