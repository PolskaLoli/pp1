array=["Genowefa","optopedał2137", "Onufry", "Celestyna", "Alojzy", "Pankracy" ]

max_name_number=0
max_name_name=""

for name in array:

    if len(name)>max_name_number:
        max_name_name=name
        max_name_number=len(name)

print(max_name_name)
