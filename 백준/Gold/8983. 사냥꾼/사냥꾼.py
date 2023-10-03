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
            return mid
    return start



M, N, L = map(int, input().split())
# M 개의 사대 위치 (X좌표값)
position = sorted(list(map(int, input().split())))

home = sorted([list(map(int, input().split())) for _ in range(N)])

cnt = 0
if M > 1:
    for x, y in home:
        shoot = binarySearch(0, M - 1, x)
        if 0 < shoot < M - 1:
            tmp = [shoot - 1, shoot, shoot + 1]
        elif 0 < shoot:
            tmp = [shoot - 1, shoot]
        elif shoot < M - 1:
            tmp = [shoot, shoot + 1]
        else:
            tmp = [shoot]
        for j in tmp:
            if abs(position[j] - x) + y <= L:
                cnt += 1
                break
else:
    for x, y in home:
        if abs(position[0] - x) + y <= L:
            cnt += 1

print(cnt)

