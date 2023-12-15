def zamiana(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j]=(i+1)*(j+1)
    

def wyswietl(array):
    for i in array:
        for j in i:
            print(j,end=" ")
        print()







if __name__=="__main__":
    array=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    zamiana(array)
    wyswietl(array)

