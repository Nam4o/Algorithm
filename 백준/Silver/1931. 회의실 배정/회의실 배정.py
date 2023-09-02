import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key= lambda x : x[1])

cnt = 1
s, e = arr[0][0], arr[0][1]

t = 1
inner = []
while t < N:
    if arr[t][0] >= e:
        if inner:
            inner.sort()
            if inner[-1][0] == inner[-1][1]:
                s, e = inner[-1][0], inner[-1][1]
                cnt += 1
                inner = []
            else:
                s, e = inner[0][0], inner[0][1]
                inner = []
        cnt += 1
        s, e = arr[t][0], arr[t][1]
    elif arr[t][1] == e:
        if [s, e] not in inner:
            inner.append([s, e])
        inner.append([arr[t][0], arr[t][1]])
    t += 1
if inner:
    inner.sort()
    if inner[-1][0] == inner[-1][1]:
        s, e = inner[-1][0], inner[-1][1]
        cnt += 1

print(cnt)