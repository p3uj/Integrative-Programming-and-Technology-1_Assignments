def primes(num):
    listOfPrimes = []
    dividend = 0
    while len(listOfPrimes) != num:
        dividend += 1   # Dividend increment by 1 every loop.
        factors = 0     # Reset the value of factors to 0 every loop.
        for divisor in range(1, dividend+1): # The first parameter is for the position to start and the last is for position to stop.
            if dividend % divisor == 0: # Check if the dividend is divisible by the value of divisor.
                factors += 1    # Count all the factors of dividend.
                if factors > 2: # Check if the factors of dividend is greater than 2, if true it is not a prime.
                    break   # Exit the for loop.
        if factors == 2:    # Check if the factors of dividend is 2, if true it is a prime.
            listOfPrimes.append(dividend)   # Add the dividend to the listOfPrimes.
    else:
        return listOfPrimes


n = 100
listOfFirstNPrimes = primes(n)  # Function call to primes function with parameter of n.
print(f"List of primes: {listOfFirstNPrimes}")