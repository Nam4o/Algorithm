T = int(input())

for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print((max(arr) - min(arr)) * 2)
