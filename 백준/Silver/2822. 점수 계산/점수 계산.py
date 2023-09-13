import sys
input = sys.stdin.readline

arr = []

for i in range(8):
    a = int(input())
    arr.append([a, i + 1])
arr.sort()

ans = 0

arr.pop(0)
arr.pop(0)
arr.pop(0)

res = []

for i in arr:
    ans += i[0]
    res.append(i[1])
res.sort()
print(ans)
print(*res)