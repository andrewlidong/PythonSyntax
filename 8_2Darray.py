# Approach 1:
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    matrix.append(row)

# Approach 2
matrix = [[0 for i in range(5)] for j in range(5)]
