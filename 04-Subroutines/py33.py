def f(n):
    wynik=" "
    for x in range(n):
        wynik += "*" 
        wynik += "/"
    
    return f"{wynik[:-1]}"

if __name__=="__main__":
    a=f(3)
    print(a)