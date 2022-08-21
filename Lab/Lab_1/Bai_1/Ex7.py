from fileinput import filename


filename = input("Input a filename: ")

extOfFile = filename.split('.')

print("The extension of the file is: " + repr(extOfFile[-1]))
