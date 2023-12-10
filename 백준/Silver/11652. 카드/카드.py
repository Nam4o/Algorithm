import sys
input = sys.stdin.readline

n = int(input())

arr = {}

for _ in range(n):
    a = int(input())
    if a in arr:
        arr[a] += 1
    else:
        arr[a] = 1

mx = max(arr.values())

ans = []
for i in arr:
    if arr[i] == mx:
        ans.append(i)

ans.sort()
print(ans[0])
