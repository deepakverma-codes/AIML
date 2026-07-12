# Lambda is a small anonymous function
square = lambda x : x*x
print(square(3))

# Factorial of any number
# ----------------------------------- #
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(8))    

#----------------------------------#
def factorial2(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial2(5))      