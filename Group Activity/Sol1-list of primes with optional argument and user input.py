"""
is_prime is the function that returns 'True' if the given argument 'num'  is greater than 1 AND if the conditions for
'num % i != 0 (If it is == 0, it is not a prime), for i in range (2,int(num**0.5)+1))  (i iterates, starting from 2, up to the square root
of the number, ** means exponentiation, n^0.5 is the square root, plus 1, so the upper bound is inclusive) are true.
"""
def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

"""
The instruction states for the default 'start' value is 2. This function will initialize the value of start to 
the input. If there was no input, it will just return the default value '2'. If there's a value, it will
return that value instead and assign it to 'start'
"""

def start(default_value):
    # The while statement is used for error handling.
    while True:
        try:    # Execute this and test for errors. If any occurs, handle them with except statement (so pupunta kay except statement).
            start = input(
                f"Start from what number? [Enter Nothing to Default to {default_value}]: ")
            if start:
                return int(start)
            else:
                return default_value
        except ValueError:  # Evaluate the error occur. If the type of error occur is 'ValueError', execute inside this statement.
            print("Invalid value!\n")


"""
This function takes the default_value as a parameter, 'count' is to track the number of items that were added to the list up to but not including 'limit'.
'num' is the 'start' on where the counting of primes will begin, and assigned the value returned by 'start'.
prime_list will hold the prime values.
'limit' is how many upper bound of the count.
If 'is_prime' returns True, meaning a prime has been found and will be appended to 'prime_list', and update 'count' and 'num'.
'num' is effectively the pointer that moves from each integer.
If 'count' is equal to the 'limit', the while loop ends, and returns 'prime_list' to 'main_list'
"""

def primes(default_value):
    num = start(default_value)

    prime_list = []
    # The while statement is used for error handling.
    while True:
        try:    # Execute this and test for errors. If any occurs, handle them with except statement (so pupunta kay except statement).
            limit = int(input("Enter how many primes the list returns: "))
            while len(prime_list) < limit:
                if is_prime(num):
                    prime_list.append(num)
                num += 1
            return prime_list
        except ValueError:  # Evaluate the error occur. If the type of error occur is 'ValueError', execute inside this statement.
            print("Invalid value!\n")

default_value = 2
main_list = primes(default_value)
print("\n")
print(f"The first {len(main_list)} primes are:")
print(main_list)