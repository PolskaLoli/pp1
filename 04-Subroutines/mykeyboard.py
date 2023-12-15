def read_number():
    try:
        a=input("podaj liczbę: ")
        return int(a)
    except ValueError: 
        print("błąd wprowadź LICZBĘ")
        return read_number()

if __name__ == "__main__":

    num1=read_number()
    num2=read_number()

    sum_result=num1+num2

    print(sum_result)