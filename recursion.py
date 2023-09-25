# Recursion -- ** demo factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# if n == 5 --> 5*4*3*2*1 = 120
n = int(input("Inter a digit: "))
print(factorial(n))
