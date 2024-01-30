t = int(input())

for tc in range(t):
    arr = sorted(list(map(int, input().split())))
    print(arr[-3])