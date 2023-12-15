def find_min_max(arr):
    rows, cols = len(arr), len(arr[0])
    
    # Initialize variables to store min and max values and their positions
    min_val = float('inf')
    max_val = float('-inf')
    min_position = (0, 0)
    max_position = (0, 0)
    
    # Iterate through the array to find min and max values and their positions
    for i in range(rows):
        for j in range(cols):
            current_value = arr[i][j]
            
            if current_value < min_val:
                min_val = current_value
                min_position = (i, j)
            
            if current_value > max_val:
                max_val = current_value
                max_position = (i, j)
    
    return min_val, min_position, max_val, max_position

# Given array
array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

# Find min and max values and their positions
min_val, min_position, max_val, max_position = find_min_max(array)

# Display the results
print(f"Smallest value: {min_val} at row {min_position[0]}, column {min_position[1]}")
print(f"Largest value: {max_val} at row {max_position[0]}, column {max_position[1]}")







if __name__=="__main__":
    array=[[-38, 19], [5,40],[-7,11],[29,16]]
    find_min_max(array)
