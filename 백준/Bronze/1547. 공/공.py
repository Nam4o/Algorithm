t = int(input())
start = 1
for tc in range(t):
    a, b = map(int, input().split())
    if a == start or b == start:
        if a == start:
            start = b
        else:
            start = a

print(start)