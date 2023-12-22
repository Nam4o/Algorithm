import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = sorted([int(input()) for _ in range(n)])

mn = float('inf')

for i in range(n):
    start = i
    next = i + 1
    check = False
    while next < n:
        if arr[next] - arr[start] >= m:
            if mn > arr[next] - arr[start]:
                mn = arr[next] - arr[start]
            check = True
            break
        next += 1
    continue

print(mn)
