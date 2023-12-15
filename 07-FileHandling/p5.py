def f(first,last):
    text=open('data.txt','r',encoding='utf-8')
    content=text.read().split()
    matching_word= [word for word in content if word.startswith(first) and word.endswith(last)]
    suma=len(matching_word)
    print(suma)









f("w","d")