def uniq(array1):
    from array import array
    unique=set(array1)
    unique_array=array("i",unique)
    return print(*unique_array)



if __name__=="__main__":
    myarray=[1,1,1,2,1,1,1]
    uniq(myarray)