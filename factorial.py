
# -*- coding: utf-8 -*-
'''
#用迭代方式写阶乘：

def factorial(n):
    result = n
    #先把阶乘的最后一位数用result表示
    #然后再用这个“最后一位数”分别乘以1, 2, 3...的方式来完成阶乘
    for i in range(1, n):
        result *= i
    return result

number = int(input('input a whole number: ',))
resultOfFactorial = factorial(number)
print("the factorial result of %d is %d. " %(number, resultOfFactorial))

'''
#用递归的方式写阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
number = int(input('input a whole number: '))
resultOfFactorial = factorial(number)
print("the factorial result of %d is %d. " %(number, resultOfFactorial))
