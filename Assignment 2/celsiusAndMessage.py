while True:
    try: # Execute and test for errors. If any occur, handle them with the except statement.
        temperature = eval(input("Enter a temperature in celsius: "))
        if temperature < -273.15: # Check if the temperature is less than -273.15.
            print("The temperature is invalid because it is below absolute zero.")
        elif temperature == -273.15: # Check if the temperature is equal to -273.15.
            print("The temperature is absolute 0.")
        elif temperature > -273.15 and temperature < 0: # Check if the temperature is between -273.15 and 0.
            print("The temperature is below freezing.")
        elif temperature == 0: # Check if the temperature is equal to 0.
            print("The temperature is at the freezing point.")
        elif temperature > 0 and temperature < 100: # Check if the temperature is between 0 and 100.
            print("The temperature is in the normal range.")
        elif temperature == 100: # Check if the temperature is equal to 100.
            print("The temperature is at the boiling point.")
        else: # Execute this if the temperature is above 100.
            print("The temperature is above the boiling point.")
        break # Exit the loop.
    except(NameError, SyntaxError): # Execute this if the user's inputted is not a number.
        print("Invalid input!")