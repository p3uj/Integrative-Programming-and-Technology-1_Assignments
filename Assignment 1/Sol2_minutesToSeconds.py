userInput = eval(input("Enter minutes: "))  # Ask user to input minutes and evaluate it (i.e int or float data type).

if userInput >= 0: # Check the user's inputted. Execute this statement if the user's inputted is not a negative number.
    print(f"The {userInput} minute/s is equivalent to {userInput * 60} second/s.")
else: # Execute this statement if the user's inputted is a negative number.
    print(f"{userInput} is not a valid minute/s.\n")