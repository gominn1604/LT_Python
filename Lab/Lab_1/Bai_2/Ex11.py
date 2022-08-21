nOfSeconds = int(input("Enter a number of seconds: "))


def convertSec(s):
    sec = 0
    min = 0
    hour = 0
    if (s < 60):
        sec = s
        print(f"{hour}:{min}:{sec}")
    elif (s < 3600 and s >= 60):
        min = int((s-s % 60)/60)
        sec = int(s % 60)
        print(f"{hour}:{min}:{sec}")
    else:
        hour = int((s-s % 3600)/3600)
        min = int(((s % 3600) - (sec % 3600) % 60)/60)
        sec = int(s-min*60-hour*3600)
        print(f"{hour}:{min}:{sec}")

convertSec(nOfSeconds)