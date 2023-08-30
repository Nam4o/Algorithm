from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

arr = deque()
for _ in range(N):
    x = list(map(int, input().split()))
    x.sort()
    arr.append(x)

lines = []

line_s, line_e = arr[0][0], arr[0][1]
arr.popleft()

if N > 1:
    while arr:
        if arr[0][0] > line_e:
            lines.append([line_s, line_e])
            line_s, line_e = arr[0][0], arr[0][1]
        if arr[0][1] < line_s:
            lines.append([line_s, line_e])
            line_s, line_e = arr[0][0], arr[0][1]
        if arr[0][0] < line_s:
            line_s = arr[0][0]
        if arr[0][1] > line_e:
            line_e = arr[0][1]
        arr.popleft()

if [line_s, line_e] not in lines:
    lines.append([line_s, line_e])

result = 0
lines.sort()
for z in range(len(lines)):
    if z < len(lines) - 1:
        if lines[z + 1][0] < lines[z][1] and lines[z + 1][1] > lines[z][1]:
            lines[z + 1][0] = lines[z][0]
        elif lines[z][0] < lines[z + 1][0] < lines[z][1] and lines[z][0] < lines[z + 1][1] < lines[z][1]:
            lines[z + 1][0], lines[z + 1][1] = lines[z][0], lines[z][1]
            continue
        else:
            result += lines[z][1] - lines[z][0]
    else:
        result += lines[z][1] - lines[z][0]

print(result)