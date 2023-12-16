import sys
input = sys.stdin.readline


N = int(input())

score = [1] * N

info = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:

            if info[i][1] < info[j][1] and info[i][0] < info[j][0]:
                score[i] += 1

print(*score)
