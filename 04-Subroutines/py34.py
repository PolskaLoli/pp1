def f(n):
    wynik=''
    for x in range(n+1):
        wynik += str(x)
    return f"{wynik[1:]}"

if __name__=="__main__":
    a=f(6)
    print(a)