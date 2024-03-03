def main():
    while True: # Execute this infinitely until the break execute.
            try: # Execute inside this statement until the user inputted is not a number.
                userInput = eval(input("Enter minutes: "))  # Ask user to input minutes and evaluate it (i.e int or float data type).
                if userInput >= 0: # Check the user's inputted. Execute this statement if the user's inputted is not a negative number.
                    print(f"The {userInput} minute/s is equivalent to {userInput * 60} second/s.")
                else: # Execute this statement if the user's inputted is a negative number.
                    print(f"{userInput} is not a valid minute/s.\n")
                    main() # Call to main function.
                break   # Exit the while loop.
            except(NameError, SyntaxError): # Execute this statement if the user's inputted is not a number.
                print("The value you've enter is not a number\n")

# Call to main function
main()