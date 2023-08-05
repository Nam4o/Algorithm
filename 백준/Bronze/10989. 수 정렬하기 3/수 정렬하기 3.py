import sys
input = sys.stdin.readline
N = int(input())
numbers = {}
for i in range(N):
    num = int(input())
    if num in numbers:
        numbers[num] += 1
    else:
        numbers[num] = 1
numbers = dict(sorted(numbers.items()))
for i in numbers:
    for j in range(numbers[i]):
        print(i)
