import math


def sumNFirstInteger(n):
    sum = 0
    for i in range(0, n+1):
        sum += i
    return sum


n = int(input("Enter a number = "))
result = math.sqrt(sumNFirstInteger(n))

print(f"Sum of square roots of first {n} integers is: {result}")
