a = int(input('enter a '))
b = int(input('enter b '))
c = int(input('enter c '))

s = ((a+b+c)/2)

import math

d = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(d)

