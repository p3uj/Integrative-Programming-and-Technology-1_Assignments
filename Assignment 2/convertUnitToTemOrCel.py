while True: # Outer loop.
    try: # Execute and test for errors. If any occur, handle them with the except statement.
        temperature = eval(input("Enter temperature: "))
        unit = input("\nWhat unit of the temperature?('C' for Celsius and 'F' for Fahrenheit): ").upper() # Ask user and convert it to uppercase.
        while unit != 'C' and unit != 'F': # Loop as long as the value of unit is not 'C' or 'F'.
            print("Invalid choice!\n")
            unit = input("What unit of the temperature?('C' for Celsius and 'F' for Fahrenheit): ").upper() # Ask user and convert it to uppercase.
        if unit == 'C': # Check if the unit is 'C'. If true, calculate and display the converted unit.
            print(f"\nCelsius = {temperature} is equivalent to Fahrenheit = {9 / 5 * temperature + 32}")
        else: # Execute this if the unit is 'F'. Calculate and display the converted unit.
            print(f"\nCelsius = {temperature} is equivalent to Fahrenheit = {5 / 9 * temperature - 32}")
        break # Exit the outer loop.
    except(NameError, SyntaxError): # Execute this if the user's inputted is not a number.
        print("Invalid value!\n")