def sort(array):
    n=len(array)
    lista1=[]
    lista2=[]    
    for i in range(n):
        if array[i]%2==0:
            lista1.append(array[i])
        else:
            lista2.append(array[i])
    listacała= lista1 + lista2
    return print(f"{listacała}")




if __name__=="__main__":
    myarray=[1,2,3,4,5,6,7,8,9]
    sort(myarray)