def f(liczba1, liczba2, operator):
    wynik=0

    if operator=="+":
        wynik=liczba1+liczba2
    elif operator=="-":
        wynik=liczba1-liczba2
    elif operator=="*":
        wynik=liczba1*liczba2
    elif operator=="**":
        wynik=liczba1**liczba2
    elif operator=="%":
        wynik=liczba1%liczba2
    return f"{wynik}"


if __name__=="__main__":
    a=f(2,3,"-")
    print(a)