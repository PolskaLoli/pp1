def find_unique_number(arr):
    # Używamy słownika do zliczania wystąpień każdej liczby w tablicy
    count_dict = {}

    # Przechodzimy przez tablicę i aktualizujemy słownik
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Szukamy liczby, która występuje tylko raz
    for num, count in count_dict.items():
        if count == 1:
            return num

# Przykład użycia
example_array = [2, 2, 3, 2, 2]
result = find_unique_number(example_array)

print(f"The unique number in the array is: {result}")
