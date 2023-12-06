import random

a = random.randrange(1,6)
print(a)

b = int(input("Guess the result of the number rolled "))



if a == b :
    print(True)
else:
    print(False)