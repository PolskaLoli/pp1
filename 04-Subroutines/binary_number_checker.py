def f(number):
    for x in number:
        if x not in ["1","0"]:
            return False
    return True

if __name__=="__main__":
    a=f("1010da1010")
    print(f"czy liczba jest binara: {a}")

