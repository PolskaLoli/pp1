fhand = open ('countries.txt',"r")
count = 0
for line in fhand :
    count=count + 1
    print (count, line, end=" " )
