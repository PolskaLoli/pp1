a=int(input('Enter product price'))
b=int(input('Enter percent discount'))

if b>=10:
    x=a-a*b/100
    print('Previous product price: ', a)
    print('Current product price',x)
    print('buy this product')
else:
    print('dont buy')


