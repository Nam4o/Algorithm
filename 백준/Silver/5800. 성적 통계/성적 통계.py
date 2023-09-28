import sys
input = sys.stdin.readline


K = int(input())

for tc in range(1, K + 1):
    print(f'Class {tc}')
    score = list(map(int, input().split()))
    p = score.pop(0)
    score.sort(reverse=True)
    max_score = score[0]
    min_score = score[-1]
    mx_gap = 0
    for i in range(1, p):
        if score[i - 1] - score[i] > mx_gap:
            mx_gap = score[i - 1] - score[i]

    print(f'Max {score[0]}, Min {score[-1]}, Largest gap {mx_gap}')