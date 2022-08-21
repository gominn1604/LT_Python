# Khong dung de quy

def fibonacciWithoutRecursive(n):
    a = 0
    b = 1
    c = 1

    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            a = b
            b = c
            c = a + b
        return c

# Dung de quy


def fibonacciWithRecursive(n):
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        return fibonacciWithRecursive(n-1) + fibonacciWithRecursive(n-2)


n = int(input("Enter a number = "))

print(f"The {n}th Fibonacci number is: {str(fibonacciWithoutRecursive(n))}")

print(f"The {n}th Fibonacci number is: {str(fibonacciWithRecursive(n))}")
