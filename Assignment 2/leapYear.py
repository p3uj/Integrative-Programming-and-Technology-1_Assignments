while True:
    try: # Execute and test for errors. If any occur, handle them with the except statement.
        year = int(input("Enter year: "))
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: # Check if it is a leap year.
            print(f"The year {year} is a leap year!")
        else:
            print(f"The year {year} is not a leap year!")
        break
    except ValueError: # Execute this if the user's inputted is not whole number.
        print("Invalid value!\n")