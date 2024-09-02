''' Make an array to store common divisors of two integers m, n.
      Check all the integers from 1 to minimum(m, n) whether they divide both m, n.
      Return the maximum number in the array.'''

def  FindGCD(m, n):
    common_divisors = []
    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            common_divisors.append(i)
    return max(common_divisors)

# test
print( FindGCD(8, 12))  
print( FindGCD(54, 24)) 
print( FindGCD(17, 13)) 
print( FindGCD(100, 10)) 
print( FindGCD(48, 180)) 

def Euclid(m, n):
    # Step 1: Check if n is 0, if so return m
    while n != 0:
        # Step 2: Calculate the remainder of m divided by n
        r = m % n
        
        # Step 3: Update m to be n, and n to be the remainder r
        m = n
        n = r
        
    # Return m as the GCD
    return m

# Testing the function with different values of m and n
print(Euclid(8, 12))    # Output: 4
print(Euclid(54, 24))   # Output: 6
print(Euclid(17, 13))   # Output: 1 (since 17 and 13 are prime to each other)
print(Euclid(100, 10))  # Output: 10
print(Euclid(48, 180))  # Output: 12
