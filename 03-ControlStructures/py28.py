a=input('Enter EAN-13 article number: ')
#b = 

if len(a)==13:
    print('Article number is correct')
    if(a[0:4]=="590"):
        print('Article manufactured in Poland')
    else:
        print("Article NOT manufactured in Poland")
else:
    print("EAN not correct")