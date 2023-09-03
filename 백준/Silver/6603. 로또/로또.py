import sys
import itertools
input = sys.stdin.readline
cnt = 0
while True:
    cnt += 1
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    k = arr.pop(0)
    arr.sort()
    cmb = itertools.combinations(arr, 6)
    for i in cmb:
        print(*i)
    print()
