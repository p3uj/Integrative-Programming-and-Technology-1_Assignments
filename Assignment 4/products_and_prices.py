"""
4.	Write a program that repeatedly asks the user to enter product names and prices. 
Store all of these in a dictionary whose keys are the product names and whose values are the prices. 
When the user is done entering products and prices, allow them to repeatedly enter a product name and 
print the corresponding price or a message if the product is not in the dictionary.
"""
from os import system
products_and_prices = {}    # Initialize an empty dictionary to store all the products and its prices.

def display_product_list():
    system('cls')   # Clear the console screen.
    print("─" * 80 + "\n" + "P R O D U C T  L I S T".center(80) + "\n" + "─" * 80)
    for product in products_and_prices:
        print(product)
    print("─" * 80)

def create_product_and_its_price():
    print("Enter 'DONE' to end the entering of product name and its price.\n" )
    while True: # Outer loop.
        product_name = input("Product Name: ").upper()

        # Validation: Loop as long as the user immediately press enter without any string.
        while product_name == "": # First Inner loop.
            print("\nInvalid value! Please enter a valid value!")
            product_name = input("Product Name: ").upper()
        
        # Check and execute if the user did not input a "DONE" for product_name.
        if product_name != "DONE":
            while True: # Second Inner loop.
                try: # Execute and test for errors. If any occur, handle them with the except statement.
                    product_price = eval(input("Product Price: "))
                    products_and_prices[product_name] = product_price   # Add the product name and its price to the dictionary.
                    break   # Exit the second inner loop
                except (NameError, SyntaxError): # Execute this if the user's inputted is not a number.
                    print("\nInvalid value! Please input a numeric value!")
        else:
            break   # Exit the Outer loop.

def main():
    another = 'Y'
    create_product_and_its_price()  # Function call to create_product_and_its_price function.
    while another == 'Y':
        display_product_list()

        # Ask user to input a product name to see its corresponding price.
        product_name = input("Product Name: ").upper()

        # Checking whether the product name is in the dictionary of products_and_prices.
        if product_name in products_and_prices:
            print(f"Product Price: {products_and_prices[product_name]}")
        else:
            print(f"{product_name} is not in the dictionary!")
        
        # Ask user if the user wants to check the price of another product.
        another = input("Do you want to check the price of another product?(Y/N): ").upper()

        # Validate the user's input.
        while another != 'Y' and another != 'N': # Loop as long as the user's input is not 'Y' or 'N'.
            print("\nInvalid input! Please input 'Y' or 'N'!")
            another = input("Do you want to check the price of another product?(Y/N): ").upper()
    system('cls')
    print("Program End!")

main()  # Function call to main function.