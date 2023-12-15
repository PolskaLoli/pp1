def f(liczba, parzyste):

    suma=0

    if parzyste==True:
        for x in str(liczba):
            if int(x)%2==0:
                suma+=int(x)
            else:
                suma+=0   
    else:
        for x in str(liczba):
            if int(x)%2!=0:
                suma+=int(x)
            else:
                suma+=0
    return f"sumą liczba jest {suma}"




if __name__=="__main__":
    a=(f(123454141,True))
    print(a)