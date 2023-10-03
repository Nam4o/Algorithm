import sys
input = sys.stdin.readline

def binarySearch(start, end, target):


    while start < end:
        mid = (start + end) // 2
        if target < position[mid]:
            end = mid - 1
        elif target > position[mid]:
            start = mid + 1
        else:
            return position[mid]
    if abs(position[mid] - target) >= abs(position[start] - target):
        if abs(position[end] - target) > abs(position[start] - target):
            return position[start]
        else:
            return position[end]
    elif abs(position[mid] - target) < abs(position[start] - target):
        if abs(position[mid] - target) < abs(position[end] -target):
            return position[mid]
        else:
            return position[end]

M, N, L = map(int, input().split())
# M 개의 사대 위치 (X좌표값)
position = sorted(list(map(int, input().split())))

home = sorted([list(map(int, input().split())) for _ in range(N)])

cnt = 0
if M > 1:
    for x, y in home:
        shoot = binarySearch(0, M - 1, x)
        if abs(shoot - x) + y <= L:
            cnt += 1
else:
    for x, y in home:
        if abs(position[0] - x) + y <= L:
            cnt += 1

print(cnt)

