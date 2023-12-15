def podzbory(array1,array2):
    n1=len(array1)
    a=""
    for i in  range(n1):
        for j in range(n1-i-1):
            if array1[j]>array1[j+1]:
                array1[j], array1[j+1] = array1[j+1], array1[j]
    

    n2=len(array2)
    for i in  range(n1):
        for j in range(n1-i-1):
            if array2[j]>array2[j+1]:
                array2[j], array2[j+1] = array2[j+1], array2[j]

    is_subset= all(item in array2 for item in array1)
    if is_subset:
        a="tablica 1 jest podzbiorem tablicy 2 "
    else:
        a="tablica 1 nie jest podzbiorem tablicy 2 "

    return f"{a}"
    
    
    


array1=[1,3,5,7,2137,9,6]
array2=[1,2,3,4,5,6,7,8,9]

print(podzbory(array1,array2))