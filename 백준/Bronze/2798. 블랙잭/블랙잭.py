import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))


result = 0
for i in range(N):
    for j in range(i + 1, N):
        inner = 0
        for k in range(j + 1, N):
            inner += arr[i] + arr[j] + arr[k]
            if inner <= M and inner > result:
                result = inner
            inner = 0

print(result)
