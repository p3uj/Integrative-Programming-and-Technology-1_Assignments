#import the tkinter module
import tkinter

#function declaration
def buttonClicked():
    #get() operation to get the value of variable assign to checkbox
    if checkVar1.get()==1:
        strSelected = "You need a wheel chair"
    else:
        strSelected = "Doesn't need a wheel chair"
    lblOutput.config(text=strSelected)

root = tkinter.Tk()
root.geometry('200x150')

#create Tkinter variable Integer
checkVar1 = tkinter.IntVar()

# check value will be stored checkVar1
chckWheelChair = tkinter.Checkbutton(root, text="Need a Wheel Chair?", variable=checkVar1).pack()

#create button widget that will call function buttonClicked
btnShow = tkinter.Button(root, text="Ok", command=buttonClicked).pack()

lblOutput = tkinter.Label(root, text="")
lblOutput.pack()

# Finally, draw the window + start the application
root.mainloop()