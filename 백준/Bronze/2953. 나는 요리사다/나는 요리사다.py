import sys
input = sys.stdin.readline

arr = [list(map(int,input().split())) for _ in range(5)]

ans = []
for i in range(len(arr)):
    ans.append([i + 1, sum(arr[i])])

ans.sort(key=lambda x: x[1])
print(*ans[-1])