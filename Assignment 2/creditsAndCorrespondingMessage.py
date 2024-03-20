while True:
    try: # Execute and test for errors. If any occur, handle them with the except statement.
        numberOfCredits = int(input("How many credits you have taken?: "))
        if numberOfCredits <= 23: # Check if the numberOfCredits are <= to 23.
            print("You are a Freshman!")
        elif numberOfCredits >= 24 and numberOfCredits <= 53: # Check if the numberOfCredits are between 24 and 53.
            print("You are a Sophomore!")
        elif numberOfCredits >= 54 and numberOfCredits <= 83: # Check if the numberOfCredits are between 54 and 83.
            print("You are a Junior!")
        else: # Execute this if the numberOfCredit is above 83.
            print("You are a Senior!")
        break # Exit the loop.
    except ValueError: # Execute this if the user's inputted is not whole number.
        print("Invalid input!\n")