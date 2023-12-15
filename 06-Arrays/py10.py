import numpy as np

def modify(array):
   

    array[0]-=1
    print(f"array po zmianie 1 {array}")



    

    array[-1]+=4
    print(f"array po zmianie 2 {array}")


    sordek=len(array)//2
    array[sordek]=array[sordek]*2
    print(f"liczba po zmianie 3 {array}")

    return



if __name__=="__main__":
    array=np.array([1,2,3,4,5])
    print(modify(array))
