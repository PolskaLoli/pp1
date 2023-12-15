def rand_elem(array):
    import random as ran
    
    przedzial=len(array)
    a=ran.randint(0,przedzial)

    return f" twoja losowa wybrana liczby z tablicy to {array[a]}"

    

array=[1,2,3,4,5,6,7,89,3,4,5,6,7,89,123]

print(rand_elem(array))