t = int(input())
for tc in range(t):
    a, b = input().split()
    a = int(a) - 1
    b = list(b)
    b.pop(a)
    print("".join(b))