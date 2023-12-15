file_path = "shopping.txt"

# Open the file in appending mode
with open(file_path, 'a') as file:
    read_product = True
    counter = 0
    
    while read_product:
        product = input("Enter product name (or press Enter to stop): ")
        
        if product != "":
            counter += 1
            # Write the product name and its number to the file
            file.write(f"{counter}. {product}\n")
        else:
            read_product = False

print("Products have been added to the shopping list.")