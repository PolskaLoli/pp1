def bubblesort(array):
    n=len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1]=array[j+1], array[j]
    return print(array)

if __name__=="__main__":
    myarray=[3,5,1,432,6,75,213]
    bubblesort(myarray)