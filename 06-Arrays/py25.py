array=[15, 8, 31, 47, 2, 19]
n=0
dlugosc=len(array)-1
suma=0


while n<=dlugosc:
    suma+=array[n] 
    n+=1
srednia=suma/(len(array)-1)
print(srednia)