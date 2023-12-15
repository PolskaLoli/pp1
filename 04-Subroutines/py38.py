def f(palindrom):
    reverse=palindrom[::-1]
    if palindrom==reverse:
        return f"ten tekst to plaindrom,"
    else:
        return f"ten tekst to nie palindrom"

p=f("kamilslimak")
print(p)