tableData = [['apples', 'oranges', 'cherries', 'banana'], #col 1
             ['Alice', 'Bob', 'Carol', 'David'],  #col 2
             ['dogs', 'cats', 'moose', 'goose']]  #col 3

print(len(tableData)) # counts columns = 3
print(len(tableData[0])) # counts rows = 4

def printTable(tableData):
    num_columns = len(tableData)  # counts total number of columns
    num_rows = len(tableData[0])  # counts total number of rows

    # Find the maximum width for each column
    colWidths = [max(len(item) for item in col) for col in tableData]

    # Print the table row-wise
    for row in range(num_rows):
        for column in range(num_columns):  # Corrected 'column' variable
            print(tableData[column][row].rjust(colWidths[column]), end=" ")  # Fixed variable
        print()  # Move to the next line after printing a row

printTable(tableData)
