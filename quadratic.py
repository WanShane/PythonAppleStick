import math

def quadratic(a, b, c):
     delta = b ** 2 - 4 * a * c
     if delta > 0:
         x1 = (- b + math.sqrt(delta)) / (2*a)
         x2 = (- b - math.sqrt(delta)) / (2*a)
         print("two answers are:")
         return x1,x2
     elif delta == 0:
         x = (- b + math.sqrt(delta)) / (2*a)
         print("just one answer:")
         return x
     else:
         return 'no answer'

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print("the numerical formula is %dx^2 + %dx + %d"%(a, b, c))
print(quadratic(a, b, c))