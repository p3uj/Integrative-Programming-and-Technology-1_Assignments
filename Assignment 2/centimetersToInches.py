length = -1 # Initialize the value of length to -1.
while length < 0: # Execute this if the length value is negative.
    try: # Execute and test for errors. If any occur, handle them with the except statement.
        length = eval(input("Enter a length in centimeters: ")) # Ask user to enter a length.
        if length >= 0: # Execute this if the value of length is not a negative.
            print(f"The inches of {length} is {round(length * 2.4, 2)}.")
        else: # Execute this if the value of length is a negative.
            print("Invalid entry!\n")
    except(NameError, SyntaxError): # Execute this if the user's inputted is not a number.
        print("Invalid value!\n")