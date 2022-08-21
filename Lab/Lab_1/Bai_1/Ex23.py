def subStringCopy(str, n):
    flen = 2
    result = ""
    if flen > len(str):
        flen = len(str)

    for i in range(n):
        result = result + str[:flen]
    return result

print(subStringCopy("danh",4))