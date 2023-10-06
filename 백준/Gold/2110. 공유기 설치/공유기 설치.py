import sys
input = sys.stdin.readline

def binary(s, e):
    global ans

    while s <= e:
        tmp = arr[0]
        cnt = 1
        mid = (s + e) // 2
        for i in range(1, N):
            if arr[i] - tmp >= mid:
                cnt += 1
                tmp = arr[i]
        if cnt >= C:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1


N, C = map(int, input().split())

arr = sorted([int(input()) for _ in range(N)])

mx = 0
ans = 0
if C == 2:
    print(arr[-1] - arr[0])
else:
    binary(1, arr[-1] - arr[0])
    print(ans)
