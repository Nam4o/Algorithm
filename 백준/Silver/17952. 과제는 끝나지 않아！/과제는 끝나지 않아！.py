import sys
input = sys.stdin.readline

N = int(input())

stack = []
score = 0
for i in range(N):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        if arr[2] - 1 == 0:
            score += arr[1]
            continue
        else:
            stack.append([arr[1], arr[2] - 1])
    else:
        if stack:
            tmp = stack.pop()
            tmp[1] -= 1
            if tmp[1] == 0:
                score += tmp[0]
                continue
            else:
                stack.append(tmp)
        else:
            continue

print(score)