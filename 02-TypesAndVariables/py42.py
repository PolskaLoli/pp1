a=input("Enter binary number: ")


a1 = int(a[0:1])
a2 = int(a[1:2])
a3 = int(a[2:3])
a4 = int(a[3:4])

if a1 == 1:
    a1 = 8
else:
    a1=0 

if a2 == 1:
    a2 = 4
else:
    a2=0 

if a3 == 1:
    a3 = 2
else:
    a3=0 

if a4 == 1:
    a4 = 1
else:
    a4=0 

print(a1 + a2 + a3 + a4)

