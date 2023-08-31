import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

arr.sort()

time = arr[0]
cnt = arr[0]
for i in range(1, len(arr)):
    time += cnt + arr[i]
    cnt += arr[i]

print(time)