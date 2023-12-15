tw=input('twitter True or False? ')
inst=input('instagram True or False? ')
yt=input('yt True or False? ')

if tw=='True' and inst=='True' or tw=='True' and yt=='True' or inst=='True' and yt=='True':
    print('persoc can be good influencer')
else:
    print('person cant be good influencer')