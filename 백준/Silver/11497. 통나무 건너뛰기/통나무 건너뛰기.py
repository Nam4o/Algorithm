from collections import deque
import sys
input = sys.stdin.readline


T = int(input())

for tc in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    sorted_arr = deque()
    sorted_arr.append(arr.pop())
    while arr:
        if arr:
            sorted_arr.append(arr.pop())
        if arr:
            sorted_arr.appendleft(arr.pop())
    mx = 0

    for i in range(1, N):
        if abs(sorted_arr[i] - sorted_arr[i - 1]) > mx:
            mx = abs(sorted_arr[i] - sorted_arr[i - 1])
    print(mx)

