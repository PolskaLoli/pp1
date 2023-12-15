def calculate_sum_from_file(file_path):    
    file=open(file_path, 'r') 
    numbers = [int(line.strip()) for line in file]
    total_sum = sum(numbers)
    return total_sum
   
# Wczytaj plik numbers.txt i oblicz sumę


if __name__=="__main__":
    file_path = 'numbers.txt'
    result = calculate_sum_from_file(file_path)


    print(f"Suma liczb z pliku '{file_path}': {result}")