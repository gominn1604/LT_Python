n = int(input("Enter a number: "))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(f"The factorial of {n} is: {factorial(n)}")