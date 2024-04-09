# Instruction: 2. Write a program that will ask user to input a list of integer tuples. Ask also for another integer value and assign it to K. Output the tuple that are divisible by K.

def find_numbers_that_divisible_by_k(user_input_tuple, divisor):
    divisible_by_k = [] # Initialize an empty list to store all the numbers that are divisible by k.
    for item in user_input_tuple:
        if item % divisor == 0: # Check and execute if the item is divisible by the divisor.
            divisible_by_k.append(item) # Add the item to the list of divisible_by_k.
    return tuple(divisible_by_k) # Return the tuple list of divisible by k to calling function.

def main():
    user_input = [] # Initialize an empty list to store all the user's inputted for integer numbers.

    # Ask user how many integer number that the user want to input.
    while True:
        try: # Execute and test for errors. If any occur, handle them with the except statement.
            limits = int(input("How many integer/s do you want to input?: "))
            break   # Exit the while loop.
        except ValueError: # Execute this if the user's inputted is not whole number.
            print("\nInvalid input! Please input an integer only!")

    # Ask user to input the integer numbers based on the limits.
    while len(user_input) != limits: # Loop as long as the length of the user_input is not equal to limits. (Outer loop)
        while True: # (Inner loop)
            try: # Execute and test for errors. If any occur, handle them with the except statement.
                user_input.append(int(input("Enter an integer number: ")))  # Add the user's input for an integer in the user_input list.
                break   # Exit the inner loop.
            except ValueError: # Execute this if the user's inputted is not whole number.
                print("\nInvalid input! Please input an integer only!")
    else: # Convert the user_input list into tuple to create a list of integer tuples.
        tuple_list = tuple(user_input)

    # Ask user to input integer number for k.
    while True:
        try: # Execute and test for errors. If any occur, handle them with the except statement.
            k = int(input("Enter an integer for k (divisible by k): "))
            break   # Exit the inner loop.
        except ValueError: # Execute this if the user's inputted is not whole number.
            print("\nInvalid input! Please input an integer only!")

    # Function call to find_numbers_that_divisible_by_k function with two parameters of tuple_list and k. Then assign the return value to divisible_by_k_tuple.
    divisible_by_k_tuple = find_numbers_that_divisible_by_k(tuple_list, k)

    # Print the tuple list that are divisible by k.
    if len(divisible_by_k_tuple) > 0:
        print(f"\nTuple list that are divisible by {k}:\n{divisible_by_k_tuple}")
    else:
        print(f"\nThere are no tuple elements that are divisible by {k}")

main()  # Function call to main function.