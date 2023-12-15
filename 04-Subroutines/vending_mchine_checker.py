def f(amount_to_pay):
    a=1
    b=2
    c=5
    liczba_5=0
    liczba_2=0
    liczba_1=0


    #while amount_to_pay>0:
    liczba_5=amount_to_pay//c
    amount_to_pay=amount_to_pay-liczba_5*c
    liczba_2=amount_to_pay//b
    amount_to_pay=amount_to_pay-liczba_2*b
    liczba_1=amount_to_pay//a
    amount_to_pay=amount_to_pay-liczba_1*a
    return f"liczba wszysktich monet {liczba_5+liczba_2+liczba_1}"
        
    
if __name__=="__main__":

    a=f(18)
    print(a)
    