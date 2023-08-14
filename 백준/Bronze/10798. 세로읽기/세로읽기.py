arr = [list(input()) for _ in range(5)]

matrix = [[''] * 15 for _ in range(5)]

for i in range(5):
    for j in range(len(arr[i])):
        matrix[i][j] += arr[i][j]

for j in range(15):
    for i in range(5):
        print(matrix[i][j], end='')
