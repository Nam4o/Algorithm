t = int(input())

for tc in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        a, b = input().split()
        if b in clothes:
            clothes[b].append(a)
        else:
            clothes[b] = [a]

    ans = 1
    for i in clothes:
        ans *= (len(clothes[i]) + 1)
    print(ans - 1)