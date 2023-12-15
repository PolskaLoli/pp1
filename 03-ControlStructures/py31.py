

x=int(input("Podaj x: "))
y=int(input("podaj y: "))

if x>0:
    if y>0:
        print("prawy górny")
    else:
        print("lewy dolny")


else:
    if y>0:
        print("lewy górany")

    else:
        print("lewy dolny")


