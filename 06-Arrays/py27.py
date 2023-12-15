def display_array_graphically(my_array):
    for x in my_array:
        t= "*" * x
        print(t)

if __name__ == "__main__":
    my_array = [12, 6, 4, 9, 10]
    display_array_graphically(my_array)