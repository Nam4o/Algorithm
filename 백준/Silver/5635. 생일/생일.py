import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    a, b, c, d = input().split()
    arr.append([a, int(b), int(c), int(d)])

arr.sort(key=lambda x:(x[3],x[2], x[1] ))
print(arr[-1][0])
print(arr[0][0])