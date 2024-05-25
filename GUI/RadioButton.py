#import the tkinter module
import tkinter

#function declaration
def buttonCkicked():
    #use get() operation for the value of variable
    intValue = varGender.get()
    if intValue == 1:
        strSelected = "You're a Male"
    elif intValue == 2:
        strSelected = "You're a Female"

    #set label text with the selected option
    lblOutput.config(text=strSelected)

root = tkinter.Tk()

#declare variable to be used by radiobutton
varGender = tkinter.IntVar()

tkinter.Label(root, text="Gender:", justify = tkinter.LEFT, padx=20).pack()

#create radiobutton widget
tkinter.Radiobutton(root, text="Male", padx=20, variable=varGender, value=1).pack(anchor=tkinter.W)
tkinter.Radiobutton(root, text="Female", padx=20, variable=varGender, value=2).pack(anchor=tkinter.W)

#create button widget
btnShow = tkinter.Button(root, text="Show Text", command=buttonCkicked).pack()

#create label widget
lblOutput = tkinter.Label(root, text="")
lblOutput.pack()

root.mainloop()