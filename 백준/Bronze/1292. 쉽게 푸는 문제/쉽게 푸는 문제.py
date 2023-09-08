import sys
input = sys.stdin.readline

numb = []
for i in range(1, 50):
    for j in range(i):
        numb.append(i)

S, E = map(int, input().split())

ans = 0

for i in range(S - 1, E):
    ans += numb[i]

print(ans)