def f(card_number):
    if len(card_number)==16:
        masked_number=card_number[:2]+"*"*10+card_number[12:17]
        return masked_number
    else:
        return f"podaj prawidłowy numer karty"
    


if __name__=="__main__":

    a=f(str(1234567891234567))
    print(a)