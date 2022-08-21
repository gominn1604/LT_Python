row = int(input("Enter the row number: "))

def printTriangle(row):
    listStar = []
    for i in range (1, row + 1):
        listStar.append("*\t" * i)
    print("\n".join(listStar))

printTriangle(row)