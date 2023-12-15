def difrent(n1,n2,n3):

    if n1!=n2 and n1!=n3 and n2!=n3:
        return f"{n1,n2,n3} are diffrent"
    else:
        return f"{n1,n2,n3} are Not diffrent"


n1=input("Enter first number: ")
n2=input("Enter second number: ")
n3=input("Enter third number: ")

result=difrent(n1,n2,n3)

print(result)