def isGrMem(grData, n):
    for value in grData:
        if n == value:
            return True
    return False

print(isGrMem([1,2,3,4], 4))