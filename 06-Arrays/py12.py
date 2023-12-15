import numpy
def liczenie(array):
    nowa_tablica=[]
    ile=0
    for i in array:
        if i%2==0:
            nowa_tablica.append(i)
            ile+=1
    return f"te liczby to {nowa_tablica} i jest ich {ile}" 



if __name__=="__main__":
    wynik=numpy.array([34,7,19,4,21,8])
    print(liczenie(wynik))

