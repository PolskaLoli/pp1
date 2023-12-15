import numpy as np 

def pri12nt(array):
    for i in array:
        print(i)

def zliczenie(array):
    rzedy=0
    kolumny=0
    for i in array:
        rzedy+=1
        for x in i:
            kolumny+=1
    return f"{rzedy} oraz {kolumny//rzedy}"

def value5(array):
    a=0
    for x in array:
        for i in x:
            if i==3:
                a+=i    
    return a


def value3(array):
    a=0
    for x in array:
        for i in x:
            if i==5:
                a+=i    
    return a

def second(array):
    #a= *array[1]
    return a


if __name__=="__main__":
    array=array=np.array([[2,5,4],[9,0,3]])
    #print(second(array))



my_array=[[2,5,4],[9,0,3]]

print("drugi wiersz to ", *my_array[1])
