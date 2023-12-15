
import numpy as np


def miesiace(miesiac):
    lista=np.lista=["styczeń","luty", "marzec","kwiecień", "maj","czerwiec","lipiec","sierpień","wrzesień","październik","listopad","gurdzień"]
    return f"Nazwa miesiąca {lista[miesiac-1]}"


if __name__=="__main__":
    wynik=miesiace(int(input("podaj nazwę miesiąca: ")))
    print(wynik)