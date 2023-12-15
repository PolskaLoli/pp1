def miesiac(n):
    miesiace =[
        "styczeń","luty","marzec","kwiecień",
        "maj","czerwiec","lipiec","sierpień",
        "wrzesień","październik","listopad","grudzień"
    ]
    if 1 <= n <= 12:
        return miesiace[n-1]
    else:
        return "Nie ma takiego miesiąca"

if __name__=="__main__": 

    a=miesiac(int(input("podaj numer miesiąca")))
    print(a)