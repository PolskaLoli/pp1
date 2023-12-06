a= float(input("enter price:  "))
b= input("enter discount in percent:  ")

suma = round(a - (int(b)/100*a), 2) 
cenaob =  round(int(b)/100*a, 2)

print("Price with disocunt: ", suma)
print("discount: ", cenaob)