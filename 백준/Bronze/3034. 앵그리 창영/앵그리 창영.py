n, w, h = map(int, input().split())
mx = ((w ** 2) + (h ** 2))
for _ in range(n):
    toach = int(input())
    if toach ** 2 <= mx:
        print("DA")
    else:
        print("NE")
        