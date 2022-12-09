import datetime

curTime = datetime.datetime.now()

s = input("birth:")
birth = int(s)
if birth >= 1990 :
    print("your age is", curTime.year - birth)
    print("you are young")
else:
    print("oh///do you feel you are old?")
