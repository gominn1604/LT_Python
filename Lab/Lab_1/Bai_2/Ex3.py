import math


fNumber = int(input("Enter a first number: "))
lNumber = int(input("Enter a last number: "))
def isPrimeNum(lNumber):
    if(lNumber<2):
        return False
    squareRoot = int(math.sqrt(lNumber))
    for value in range(2, squareRoot+1):
        if(lNumber % value == 0):
            return False
    return True

sb=""
for i in range (fNumber, lNumber+1):
    if (isPrimeNum(i)):
        sb = sb + str(i) + " "
    i = i + 1
print(sb)

