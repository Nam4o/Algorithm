import itertools
import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())

arr = input().split()

arr.sort()
a = combinations(arr, L)

ans = []
for i in a:
    gather_count = 0
    gather_count += i.count('a')
    gather_count += i.count('e')
    gather_count += i.count('i')
    gather_count += i.count('o')
    gather_count += i.count('u')

    if gather_count == 0 or gather_count > L - 2:
        continue
    else:
        ans.append(sorted(i))

for j in ans:
    print(''.join(j))