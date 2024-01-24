t = int(input())

for tc in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop(0)
    arr.pop()
    ans = sum(arr)
    if arr[-1] - arr[0] >= 4:
        ans = "KIN"
    print(ans)