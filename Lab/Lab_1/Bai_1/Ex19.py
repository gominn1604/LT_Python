def newString(string):
    return string if len(string) >= 2 and string[:2] == "Is" else "Is" + string

print(newString("danh"))