array=[34,7,19,4,21,8,123,51,24,42,86]

Index=0
count=0

while Index<len(array):
    if array[Index]%2==0:
        count+=1
    Index+=1

print(f"{count} and how many number {Index}")

