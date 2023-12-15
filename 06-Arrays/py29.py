def comaper(array1,array2):
    result=[]
    result2=[]
    for number in array1:
        if number not in array2:
            result.append(number)

    for number2 in array2:
        if number2 not in array1:
            result2.append(number2)
    return print(f"Liczby nie występujące w tablicy numer dwa to: {result}, a liczby z tabeli 2 niewystępujące w tabeli 1 to {result2}")

    



if __name__=="__main__":
    array1=[4,36,12,28,9,44,5]   
    array2=[5,1,36,2137]
    comaper(array1,array2)