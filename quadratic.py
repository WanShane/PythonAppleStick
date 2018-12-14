#ax^2+bx+c=0:

import math

def quadratic(a, b, c):
    deta = pow(b,2)-4*a*c
    if deta < 0:
        print('no answer')
    if deta == 0:
        return -b/(2*a)
    else:
        return (-b+(math.sqrt(deta)))/(2*a),(-b-(math.sqrt(deta)))/(2*a)
    
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
print('quadratic:',quadratic(a, b, c))
