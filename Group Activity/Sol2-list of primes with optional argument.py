def getFactors(dividend):
    numOfFactors = 0
    for divisor in range(1, dividend+1): # The first parameter is for the position to start and the last is for position to stop.
        if dividend % divisor  == 0: # Check if the dividend is divisible by the value of divisor.
            numOfFactors += 1 # Count all the factors of dividend.
            if numOfFactors > 2: # Check if the factors of dividend is greater than 2, if true it is not a prime.
                return numOfFactors
    return numOfFactors
    
def primes(n=100, start=2):
    listOfPrimes = []
    dividend = start	# Starting number to evaluate if it is a prime or not.
    while len(listOfPrimes) < n:
        if getFactors(dividend) == 2:    # Function call to getFactors function. Then check if the return value is equal to 2, if true it is a prime.
            listOfPrimes.append(dividend)   # Add the dividend to the listOfPrimes.
        dividend += 1	# Increment dividend by 1 for the next evaluation.
    else:
        return listOfPrimes

print(f"The first {len(primes(100,11))} primes are:\n{primes(100, 11)}\n")    # First usage: Function call to primes function with 2 parameters (100 for n and 11 for start).
print(f"The first {len(primes(50, 20))} primes are:\n{primes(50, 20)}")    # Second usage: Function call to primes function with 2 parameters (50 for n and 20 for start).