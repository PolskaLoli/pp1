def compar(array1,array2):
    dlugosc1=len(array1)
    dlugosc2=len(array2)    
    if dlugosc1==dlugosc2:
        #print("ok")
        war1=True
    else: 
        war1=False
        
    
    for i in range(len(array1)):
        if array1[i]!=array2[i]:
            war2=False
            break
        else:
            war2=True
    
    if war1==war2:
        print("tablice są identyczne")
    else:
        print("tablice nie są identyczne")






if __name__=="__main__":
    array1=["water","book","sky"]   
    array2=["water","book","sky","PIS"]
    compar(array1,array2)