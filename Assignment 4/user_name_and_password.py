"""
5.	Write a program that uses a dictionary that contains ten user names and passwords. 
The program should ask the user to enter their username and password. If the username is not in the dictionary, 
the program should indicate that the person is not a valid user of the system. If the username is in the dictionary, 
but the user does not enter the right password, the program should say that the password is invalid. 
If the password is correct, then the program should tell the user that they are now logged in to the system.
"""
from os import system   # Module in order to work the clear screen.
user_authentication = {
    "user 1": "user1password",
    "user 2": "user2password",
    "user 3": "user3password",
    "user 4": "user4password",
    "user 5": "user5password",
    "user 6": "user6password",
    "user 7": "user7password",
    "user 8": "user8password",
    "user 9": "user9password",
    "user 10": "user10password"
}

def check_user_credentials(user_name):
    # Check and execute if the parameter of user_name is in the dictionary called user_authentication.
    if user_name in user_authentication:
        # Ask user to input the password then check and execute if the entered password is match to the password of the user_name.
        if user_authentication[user_name] == input("Password: "):
            return True # Return true to calling function.
        else:
            exit("Invalid password!")   # Exit the program with the message of "Invalid password!".
    else: # Execute this if the user_name is not in the dictionary called user_authentication.
        return False    # Return false to calling function.

def main():
    print("─" * 80 + "\n" + "A C C O U N T S   D I C T I O N A R Y   P Y T H O N".center(80) + "\n" + "─" * 80)

    # Ask the user to input the username then function call to check_user_credentials function with an argument of the user's inputted for the username.
    if check_user_credentials(input("Username: ")): # Execute this if the return value is true.
        system('cls')   # Clear the console screen.
        print("─" * 80 + "\n" + "YOU ARE NOW LOGGED IN TO THE SYSTEM!".center(80) + "\n" + "─" * 80)
    else:   # Execute this if the return value is false.
        print("You are not a valid user of the system!")

main()  # Function call to main function.