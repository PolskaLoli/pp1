def sort(array):
    n=len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array









if __name__=="__main__":
    array=[1,4,6,3,2,6,1,-12]
    print(sort(array))