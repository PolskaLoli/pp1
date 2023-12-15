def converd_2d(array):
    arrad_1d=[]
    for x in array:
        for y in x:
            arrad_1d.append(y)
    return print(arrad_1d)



if __name__=="__main__":
    array=[
        [2,3],
        [1,5]
    ]

    converd_2d(array)