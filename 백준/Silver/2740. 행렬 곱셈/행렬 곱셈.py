import sys
input = sys.stdin.readline

NA, MA = map(int, input().split())
matrixA = [list(map(int, input().split())) for _ in range(NA)]
NB, MB = map(int, input().split())
matrixB = [list(map(int, input().split())) for _ in range(NB)]


arr = [[0 for _ in range(MB)] for _ in range(NA)]

for i in range(NA):
    for j in range(MB):
        for k in range(MA):
            arr[i][j] += matrixA[i][k] * matrixB[k][j]

for u in arr:
    print(*u)