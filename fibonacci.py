# 斐波那契 e.g.
# 1 2 3 4 5 6  7  8  9 ...
# 1 1 2 3 5 8 13 21 34 ...

#用迭代的方式实现斐波那契的结果：
def fib(n):
    n1 = 1
    n2 = 1
    n3 = 1
    
    if n < 1:
        print("Wrong!")
        return -1
    
    while (n-2) > 0:
        n3 = n1 + n2
        n1= n2
        n2 = n3
        n = n-1
    return n3

inputNumber = int(input("input the number:"))
result = fib(inputNumber)
print("the fibonacci result is: %d" % result)

'''
#用递归的方式
##(￣Д￣)ﾉ 递归调用既花时间又耗内存...
def fib(n):
    if n < 1:
        print("Wrong!")
        return -1
    if n == 1 or n ==2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)

inputNumber = int(input("input the number:"))
result = fib(inputNumber)
print("the fibonacci result is: %d" % result)

'''