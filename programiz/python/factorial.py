# Finding the factorial of a number

def factorial_num(n):
    # initializing factorial
    fact = 1
    # starts at 1 and ends at 4: this includes 4 because python ends at a number below the last index
    for i in range(1, n+1):
        fact = fact * i
    return fact


print(factorial_num(4))


