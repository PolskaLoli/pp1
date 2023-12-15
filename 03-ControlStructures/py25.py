a=int(input('number of product'))
b=int(input('product price'))
c=a*b 

if a>=2:
    x=c-c*25/100
    print('you must pay',x)
else:
    print('chuj')