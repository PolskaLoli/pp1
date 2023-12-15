
n=12
def to_bin(n):
    remin=""
    while n>0:
        remin=""
        remin=str(n%2)+remin
        n=n//2
    return remin

print(to_bin)