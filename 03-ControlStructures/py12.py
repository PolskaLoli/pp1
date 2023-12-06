firstname=input("Enter first person name ")
firstage=int(input('Enter first person age'))

secondname= input('enter second person name ')
secondage= int(input('enter second person age '))


if firstage>18 and secondage>18:
    print(firstname, 'and' , secondname, 'have 18y')
else:
    print(firstname, 'and', secondname, 'dont have 18')