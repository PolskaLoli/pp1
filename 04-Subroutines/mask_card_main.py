import mask_card_number

numer=str(input("Podaj numer karty kredytowej do zamaskowania"))
wynik=mask_card_number.f(numer)
print(numer,"  zamaskowane:   ",wynik)