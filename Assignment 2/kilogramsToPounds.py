while True: # Outer loop.
    try: # Execute and test for errors. If any occur, handle them with the except statement.
        kilograms = eval(input("Enter weight(kilograms): ")) # Ask user to input weight.
        while kilograms < 0: # Loop as long as the value of kilograms is a negative. (Inner loop)
            kilograms = eval(input("Invalid input!\n\nEnter weight(kilograms): "))
        print(f"The pounds of {kilograms} kilograms is {kilograms * 2.2046226218}") # Calculate and display.
        break # Exit the outer loop.
    except(NameError, SyntaxError): # Execute this if the user's inputted is a number.
        print("Invalid input!\n")