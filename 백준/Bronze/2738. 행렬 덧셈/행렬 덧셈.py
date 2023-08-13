N, M = map(int, input().split())

arr_A = [list(map(int, input().split())) for _ in range(N)]
arr_B = [list(map(int, input().split())) for _ in range(N)]

arr_C = []
for i in range(N):
    stack = []
    for j in range(M):
        stack.append(arr_A[i][j] + arr_B[i][j])
    arr_C.append(stack)

for k in range(N):
    print(*arr_C[k])