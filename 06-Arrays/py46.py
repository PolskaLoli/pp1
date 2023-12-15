def zliczanie(array):
    for row in array:
        for value in row:
            print(value, end=' ')
        print()







if __name__=="__main__":
    array=[
        [1,2],
        [3,4],
        [5,6],
        [7,8]
    ]

    print(zliczanie(array))