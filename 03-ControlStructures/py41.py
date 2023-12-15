
def f(a):
    kod="0805"
    pop=""
    niepop="Sorry, your payment card has been blocked"
    proby=1
    c=0
    while proby<3:
        if kod==a:
            print("kod poprawny")
            return pop
            

        
        else:
            a=input("podaj poprawny kod")
            proby+=1
    return niepop   
print(f(input("podaj Kod: ")))