def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

x = int(input("input the number which to power:"))
n = int(input("input the times:"))

print("the result is：",power(x,n))