import sys
input = sys.stdin.readline

def binary(s, e):
    global mx, alkali, acid

    while True:
        if s >= e:
            return
        n = abs(arr[s] + arr[e])
        if n < mx:
            mx = n
            alkali = arr[s]
            acid = arr[e]
        if n > abs(arr[s + 1] + arr[e]):
            s += 1
        elif n > abs(arr[s] + arr[e - 1]):
            e -= 1
        else:
            s += 1
            e -= 1


N = int(input())

arr = sorted(list(map(int, input().split())))

mx = float('inf')

alkali = 0
acid = 0

binary(0, N - 1)

print(alkali, acid)
