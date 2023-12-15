def secondL(array1):
    n=len(array1)
    for i in range(n):
        for j in range(0,n-i-1):
            if array1[j]>array1[j+1]:
                array1[j], array1[j+1]=array1[j+1], array1[j]
    return print(array1[-2])

def diff(array1):
    n=len(array1)
    for i in range(n):
        for j in range(0,n-i-1):
            if array1[j]>array1[j+1]:
                array1[j], array1[j+1]=array1[j+1], array1[j]
    return print(f"{array1[-1]-array1[0]}")

def mediana(array1):
    n=len(array1)
    for i in range(n):
        for j in range(0, n-i-1):
            if array1[j]>array1[j+1]:
                array1[j], array1[j+1]= array1[j+1], array1[j]
    
    if n%2==0:
        middle1=array1[n//2]
        middle2=array1[n//2-1]
        return print(f"{(middle1+middle2)/2}")

    else:

        middle3=array1[n//2]
        return print(f"{middle3/2}")
    
def mniejszwiększatablica(array1):
    n=len(array1)
    for i in range(n):
        for j in range(0,n-i-1):
            if array1[j]>array1[j+1]:
                array1[j], array1[j+1]=array1[j+1], array1[1]
    array2ele=(array1[0],array1[-1])            
    
    return print(f"{array2ele}")


def odzielone(array1):
    n=len(array1)
    string=" "
    for i in range(0,n):
        string += str(array1[i])
        if i<n-1:
            string+="-"


    return print(f"{string}")


if __name__=="__main__":
    myarray=[2,5,7]
    odzielone(myarray)