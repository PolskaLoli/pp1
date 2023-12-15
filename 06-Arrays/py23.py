array=[-15, 8, -31, 47, -2, 19]

min_number=array[0]
max_number=array[0]
for x in array:
    if x > max_number:
        max_number=x
    if x < min_number:
        min_number=x

print(min_number)
print(max_number)