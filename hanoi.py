#汉诺塔
#用递归的方式写最佳，思路是，从后往前推
#n：盘子的数量
#x, y, z：定义汉诺塔的三根针
def hanoi(n, x, y, z):
    if n == 1:
        print(x, "-->", z)
    else:
        hanoi(n-1, x, z, y)#将(n-1)【个】盘子，从x针移到y针
        print(x, "-->", z)#将x针上最底下的盘子，移到z针
        hanoi(n-1, y, x, z)#将y针上的(n-1)【个】盘子，移到z针

n = int(input("input how many storeys does the hanoi have: "))
hanoi(n, 'x', 'y', 'z')