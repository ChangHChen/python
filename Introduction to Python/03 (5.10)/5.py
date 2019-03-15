matrix = [[75, 51, 61, 61, 81],
          [68, 39, 14, 17, 15],
          [48, 51, 351, 15, 1],
          [15, 32, 16, 14, 60]]
print("matrix =", matrix)
result = []
for column in range(len(matrix[0])):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][column]
    result.append(total)
print("result =", result)