import sys
input = sys.stdin.readline

amount = int(input())
for i in range(2):
    num = int(input())
    amount *= num
amount = str(amount)
for j in range(10):
    print(amount.count(f'{j}'))