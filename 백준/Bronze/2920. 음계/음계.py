import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

check = True
if arr[0] == 1:
    i = 1
    while i != len(arr):
        if arr[i] - arr[i - 1] != 1:
            check = False
            break
        i += 1
    if check:
        print('ascending')
    else:
        print('mixed')
elif arr[0] == 8:
    i = 1
    while i != len(arr):
        if arr[i - 1] - arr[i] != 1:
            check = False
            break
        i += 1
    if check:
        print('descending')
    else:
        print('mixed')
else:
    print('mixed')