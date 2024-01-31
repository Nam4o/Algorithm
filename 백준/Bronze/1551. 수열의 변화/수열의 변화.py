n, k = map(int, input().split())
arr = list(map(int, input().split(",")))

for i in range(k):
    tmp = []
    for j in range(1, n - i):
        tmp.append(arr[j] - arr[j - 1])
    arr = tmp
ans = ""
for k in range(len(arr)):
    if k != len(arr) - 1:
        ans += str(arr[k]) + ","
    else:
        ans += str(arr[k])

print(ans)