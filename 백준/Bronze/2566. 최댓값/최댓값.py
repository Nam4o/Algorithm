arr = [list(map(int, input().split())) for _ in range(9)]

mx_num = 0
mx_i = 0
mx_j = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] >= mx_num:
            mx_num = arr[i][j]
            mx_i = i
            mx_j = j
print(mx_num)
print(mx_i + 1, mx_j + 1)