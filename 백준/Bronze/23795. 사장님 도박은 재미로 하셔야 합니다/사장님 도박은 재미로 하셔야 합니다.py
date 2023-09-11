import sys

input = sys.stdin.readline

amount = 0

while True:
    num = int(input())
    if num == -1:
        print(amount)
        break
    else:
        amount += num