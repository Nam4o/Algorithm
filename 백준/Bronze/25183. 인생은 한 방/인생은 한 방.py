import sys
input = sys.stdin.readline

N = int(input())

arr = input().strip()

cnt = 1
for i in range(1, len(arr)):
    if cnt == 5:
        break
    if ord(arr[i - 1]) + 1 == ord(arr[i]) or ord(arr[i - 1]) - 1 == ord(arr[i]):
        cnt += 1
    else:
        cnt = 1

if cnt == 5:
    print('YES')
else:
    print('NO')