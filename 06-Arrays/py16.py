array=[[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
a=0
for x in array:
    for i in x:
        if i%2!=0:
            a+=i
print(a)