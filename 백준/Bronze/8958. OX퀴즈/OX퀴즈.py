import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    arr = input().strip()
    i = 1
    if arr[0] == 'O':
        score = 1
    else:
        score = 0
    cnt = 0
    while i != len(arr):
        if arr[i] == 'O':
            if arr[i] == arr[i - 1]:
                cnt += 1
            else:
                cnt = 0
            score += 1 + cnt
        i += 1
    print(score)