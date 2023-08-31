import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}

for _ in range(N):
    a, b = input().split()
    dic.setdefault(a, b)

for i in range(M):
    c = input().strip()
    print(dic[c])
