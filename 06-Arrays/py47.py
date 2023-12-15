array= [[7,3,7,9,0],
        [2,9,0,1,5],
        [3,8,6,4,7],
        [8,7,1,1,5]]
x=len(array)

#print(x)

a=[]
for j in array:
    a.append(j[-1])
    
    print(j[-1])

print("suma cyfr ostatniej kolumny jest równa: ",sum(a))
   
