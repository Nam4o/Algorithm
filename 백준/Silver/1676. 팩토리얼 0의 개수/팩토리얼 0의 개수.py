import sys
input = sys.stdin.readline

N = int(input())

a = N

for i in range(1, N):
    a *= i

a = str(a)

cnt = 0
for j in range(1, len(a)):
    if a[-j] != '0':
        break
    if a[-j] == '0':
        cnt += 1

print(cnt)