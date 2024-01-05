import sys
input = sys.stdin.readline

n = int(input())
crain = sorted(list(map(int, input().split())), reverse=True)

m = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)

cnt = 0
i = 0
j = 0
if crain[0] < boxes[0]:
    cnt = -1
else:
    while boxes:
        if j == len(boxes):
            j = 0
            i = 0
            cnt += 1
        if i < n and crain[i] >= boxes[j]:
            boxes.pop(j)
            i += 1
        else:
            j += 1

        if i == n:
            i = 0
            j = 0
            cnt += 1
    if i != n and i != 0:
        cnt += 1
print(cnt)