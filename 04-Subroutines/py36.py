def f(detector):
    osoby=0
    for x in detector:
        if x=="+":
            osoby+=1
        else:
            osoby-=1
    if osoby<0:
        return f"Debilu jak z pomieszczenia może wyjść osoba która nie weszła"
    return f"ilość osób {osoby}" 
        

if __name__=="__main__":
    a=f("+--+--+")
    print(a)