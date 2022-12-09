print('------Let us play game------')
temp = input("let's guess that which number I am thinking: ")
guess = int (temp)
if guess == 8:
    print("How did you get that!")
    print("But there's no bonus")
else:
    print("ouch, you lost the game")
print("Bye-bye. Game is over")
