import sys

input = sys.stdin.readline

n = int(input())
sum = 0
for i in range(n):
    plug = int(input())
    sum += plug - 1
print (sum + 1)