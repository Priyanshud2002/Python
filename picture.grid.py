grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Get the number of columns (from the first row)
for col in range(len(grid[0])):  # Loop through each column (0 to 5)
    for row in range(len(grid)):  # Loop through each row (0 to 8)
        print(grid[row][col], end='')  # Print the character without a new line
    print()  # Print a new line after each column is printed
