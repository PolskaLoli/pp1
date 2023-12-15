def occurs(number, array):
    for n in array:
        if number==n:
            return f"{number} znajduje się w tablicy "
        else:
            return f"{number} nie znajduje się w tablicy "


if __name__=="__main__":
    myarray=[15, 38, 7, 23, 14]
    number=15
    print(occurs(number,myarray))