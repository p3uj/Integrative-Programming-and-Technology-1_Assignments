def getFactors(dividend):
    numOfFactors = 0
    for divisor in range(1, dividend+1): # The first parameter is for the position to start and the last is for position to stop.
        if dividend % divisor  == 0: # Check if the dividend is divisible by the value of divisor.
            numOfFactors += 1 # Count all the factors of dividend.
            if numOfFactors > 2: # Check if the factors of dividend is greater than 2, if true it is not a prime.
                return numOfFactors
    return numOfFactors

def primes(n=100):
    listOfPrimes = []
    dividend = 0
    while len(listOfPrimes) != n:
        dividend += 1	# Increment dividend by 1 for every loop to evaluate.
        if getFactors(dividend) == 2:    # Function call to getFactors function. Then check if the return value is equal to 2, if true it is a prime.
            listOfPrimes.append(dividend)   # Add the dividend to the listOfPrimes.
    else:
        return listOfPrimes

print(f"The first {len(primes())} primes are:\n{primes()}\n")	# First usage: Function call to primes function with no parameter (default value).
print(f"The first {len(primes(10))} primes are:\n{primes(10)}")	# Second usage: Function call to primes function with parameter 10.