import random
secret = random.randint(1, 10)

print('-----------------this is My Game-----------------')
temp = input("Let's guess which number is in my mind now!\nYou'll have 3 times to guess the number.\n")
guess = int(temp)
times = 0

if guess == secret:
    print("OMG, you got it. ")
    print("There is no bonus at all. ")

while (guess != secret) and (times < 2):
    #guess = int(temp)
    if guess > secret:
        print("NoNoNo, it should be a litte one. ")
    elif guess < secret:
        print("Hey, it should be a bigger one. ")
    times = times + 1
    temp = input("And you have a more chance.\n")
print("Times up, game over. ")