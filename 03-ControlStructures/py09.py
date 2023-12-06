maxpoint= int(input('enter max point from exam '))
tpoint = int(input('enter exam points '))/maxpoint*100  


if tpoint > 50:
    print('you pass test and you earn', round(tpoint,2),'%')
else:
    print('you dont pass')

#print(round(tpoint,2),'%')

