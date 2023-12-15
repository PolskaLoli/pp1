import random

a=random.randint(1,30)

if a%3==0:
    print(a,"Three")


if a%5==0:
    print(a,"Five")


if a%5==0 and a%3==0:
    print(a,"Bingo")

if a%5!=0 and a%3!=0:
    print(a)
