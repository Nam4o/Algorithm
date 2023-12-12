import sys
input = sys.stdin.readline

amount = 0
mn = float('inf')

for i in range(7):
    a = int(input())
    if a % 2 == 1:
        amount += a
        if a < mn:
            mn = a

if amount != 0:
    print(amount)
    print(mn)
else:
    print(-1)