def numberintext(text):
    word = text.split()
    return f"liczba wyrazów w teksicie to: {len(word)}"

def lenght1(text):
    word = text.split()
    n= len(word)
    for i in range(n):
        for j in range(0,n-i-1):
            if len(word[j])>len(word[j+1]):
                word[j], word[j+1]=word[j+1], word[j]
    return f"{word[::-1]}"

def alphabetical(text):
    word = text.split()
    n= len(word)
    for i in range(n):
        for j in range(0,n-i-1):
            if word[j]>word[j+1]:
                word[j], word[j+1]=word[j+1], word[j]
    return f"{word}"
    










if __name__=="__main__":
    text="An apple a day keeps the doctor away"
    print(alphabetical(text))