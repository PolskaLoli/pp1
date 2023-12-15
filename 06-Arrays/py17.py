array=[[0,0,0],[0,0,0],[0,0,0]]

# Dane tablicy

for i in range(len(array)):
    array[i][i]=1

for x in array:
    print(x)