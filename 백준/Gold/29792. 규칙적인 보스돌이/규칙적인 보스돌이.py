import sys
input = sys.stdin.readline
from itertools import combinations

N, M, K = map(int, input().split())

D = sorted([int(input()) for _ in range(N)], reverse=True)

boss = [list(map(int, input().split())) for _ in range(K)]


total = 0
chr = 0
while chr < M:
    mx = 0

    for i in range(1, K + 1):
        a = list(combinations(boss, i))

        for j in range(len(a)):
            time = 900
            amount = 0
            hp = D[chr]
            for w in a[j]:

                if w[0] % D[chr] != 0:
                    time -= w[0] // D[chr] + 1
                else:
                    time -= w[0] // D[chr]
                amount += w[1]

                if time < 0:
                    amount = 0
                    break
                elif time == 0:
                    if amount > mx:
                        mx = amount
                        break

            if amount > mx:
                mx = amount
    total += mx
    chr += 1
print(total)
