array = 2, 3, 7, 5, 4,

print("Array: ",array)
print(f"Number of argument: {len(array)}")
print(f"first value: {array[0]}")
print(f"second value: {array[1]}")
print(f"last value: {array[-1]}")
print(f"last but one value {array[3]}")
print(f"sum first and last value is: {array[0]+array[-1]}")
middle_array=array[len(array)//2]
print(middle_array)

for x in array:
    print(x,"",end="")

