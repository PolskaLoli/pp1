def program(array,liczba):
    liczba_ele=0
    n=len(array)
    if liczba>n:
        return print(f"Podana liczba jest większa niż liczba elementów tablicy:)")
    for i in range(n):       
        if array[i] > liczba:
            liczba_ele+=1
    return  print(f"{liczba_ele}")





if __name__=="__main__":
    array=[1,2,3,4,5,6,7,8,9]
    liczba=int(input("Podaj liczbę: "))
    program(array,liczba)