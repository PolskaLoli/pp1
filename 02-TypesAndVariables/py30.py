import random

a = random.randrange(1,6)

print(a)

if a == 1 or a==6:
    a=True
    print("special number is: " + str(a))

else:
    a=False
    print("special number is: " + str(a))
    
    