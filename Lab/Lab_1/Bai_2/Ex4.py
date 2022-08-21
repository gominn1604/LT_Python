import math


n = int(input("Enter a number: "))

def checkPerfectSquare(m):
    n = int (math.sqrt(m)) 
    return n * n == m 

def checkFibo(m): 
    return checkPerfectSquare(5 * m * m + 4) or checkPerfectSquare(5 * m * m - 4) 

if (checkFibo(n) == True): 
    print (n, "is the Fibonacci number") 
else: 
    print (n , "is not the Fibonacci number")