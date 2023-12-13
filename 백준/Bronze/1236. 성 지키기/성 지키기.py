n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
a = 0
b = 0
for i in range(n):
    if arr[i].count(".") == m:
       a += 1

for j in range(m):
    cnt = 0
    for t in range(n):
        if arr[t][j] == ".":
           cnt += 1
    if cnt == n:
        b += 1


print(max(a, b))
