def getFactors(num):
    factors = []    # Initialize the list to empty.
    for divisor in range(1, abs(num)+1):    # The first parameter is for the position to start and the last is for position to stop. Abs method is used to return the absolute value.
        if num % divisor == 0:  # Check and execute if the num is divisible by the divisor.
            factors.append(divisor) # Add the divisor to the list.
            if num < 0: # Check and execute if the num is a negative.
                factors.append(-divisor)   # Add the negative value of divisor to the list.
    return factors  # Return the list to the calling function.

while True:
    try: # Execute and test for errors. If any occur, handle them with the except statement.
        integer = int(input("Enter an integer: "))
        if integer != 0:    # Check and execute if the user inputted is not a zero.
            factors = getFactors(integer)   # Function call to the getFactors function with parameter of integer. Then assign the return value to factors.
            print(f"List of factors of the {integer}: {factors}")
        else:
            print("0 has no factors!")
        break
    except ValueError: # Execute this if the user's inputted is not whole number.
        print("\nInvalid input! Please enter an integer only!")
