def create_2d_arr(x,y):
    return [[0 for _ in range(x)] for _ in range(y)]  


def display(array):
    for x in array:
        for y in x:
            print(y,end=" ")
        print()







if __name__=="__main__":
    x=5
    y=3
    array=create_2d_arr(x,y)

    display(array)





