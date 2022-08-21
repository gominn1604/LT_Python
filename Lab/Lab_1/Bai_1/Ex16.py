n = int(input("Input n: "))

def diff(n):
    if n < 17:
        return 17-n
    else:
        return abs(17-n)*2

print(diff(n))