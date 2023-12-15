def f(first):
    text=open('data.txt','r', encoding="utf-8")
    content=text.read().split()

    matching_word=[word for word in content if len(word)==first]
    sum=len(matching_word)

    print(sum)



f(4)