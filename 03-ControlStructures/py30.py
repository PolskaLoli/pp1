time=input("Enter time (24-hour format 00:00): ")
a=int(time[0:2])

#time2=

if a>12:
    b=a-12
    print(b,":",time[3:5],"AM")

else:
    print(time,"AM")



