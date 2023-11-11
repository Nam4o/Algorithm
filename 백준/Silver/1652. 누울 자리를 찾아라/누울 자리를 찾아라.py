import sys
input = sys.stdin.readline


N = int(input())

arr = [list(input().strip()) for _ in range(N)]



linear = 0
vertical = 0

for i in range(N):
    check = False
    inner_cnt = 0
    for j in range(N):
        if check == False:
            if arr[i][j] == ".":
                check = True
                inner_cnt += 1
        else:
            if arr[i][j] == ".":
                inner_cnt += 1
            else:
                if inner_cnt >= 2:
                    linear += 1
                check = False
                inner_cnt = 0
    if inner_cnt >= 2:
        linear += 1

for i in range(N):
    check = False
    inner_cnt = 0
    for j in range(N):
        if check == False:
            if arr[j][i] == ".":
                check = True
                inner_cnt += 1
        else:
            if arr[j][i] == ".":
                inner_cnt += 1
            else:
                if inner_cnt >= 2:
                    vertical += 1
                check = False
                inner_cnt = 0
    if inner_cnt >= 2:
        vertical += 1

print(linear, vertical)

