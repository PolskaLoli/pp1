def print_pattern(rows):
    for i in range(1, rows + 1):
        print("* " * i)

    for i in range(rows - 1, 0, -1):
        print("* " * i)

# Ustaw ilość wierszy
rows = 7
print_pattern(rows)


