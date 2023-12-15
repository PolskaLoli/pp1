def veinding(amount):
    
    while amount>0:
        suma_5=amount//5
        amount=amount-5*suma_5
        suma_2=amount//2
        amount=amount-2*suma_2
        suma_1=amount//1
        amount=amount-1*suma_1
        print("ilość pięciozłotówek",suma_5)
        print("ilość dwuzłotówek",suma_2)
        print("ilość jednozłotuwek",suma_1)
    

veinding(2137)

#amount = int(input("Podaj cene: "))





