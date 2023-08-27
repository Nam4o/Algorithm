import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [input().strip() for _ in range(N)]

base1 = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
         ]
base2 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
         ]

result = 10000000000000000

for i in range(N - 7):
    for j in range(M - 7):
        cnt1 = 0
        cnt2 = 0
        if arr[i][j] == 'W':
            for k in range(i, i + 8):
                for t in range(j, j + 8):
                    if cnt1 > result and cnt2 > result:
                        continue
                    if arr[k][t] != base1[k - i][t - j]:
                        cnt1 += 1
                    if arr[k][t] != base2[k - i][t - j]:
                        cnt2 += 1
        elif arr[i][j] == 'B':
            for k in range(i, i + 8):
                for t in range(j, j + 8):
                    if cnt1 > result and cnt2 > result:
                        continue
                    if arr[k][t] != base2[k - i][t - j]:
                        cnt2 += 1
                    if arr[k][t] != base1[k - i][t - j]:
                        cnt1 += 1
        if cnt1 < result:
            result = cnt1
        if cnt2 < result:
            result = cnt2

print(result)