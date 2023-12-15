def reverse_tuple(tupple1):
    rev_tup=tuple(reversed(tupple1))
                  
    return f"{rev_tup}"
        





if __name__=="__main__":
    tuple1=(10,20,30,40,50) 
    print(reverse_tuple(tuple1))