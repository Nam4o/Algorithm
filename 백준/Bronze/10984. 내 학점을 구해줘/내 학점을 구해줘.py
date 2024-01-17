t = int(input())

for tc in range(t):
    n = int(input())
    amount = 0
    gpa = 0
    for _ in range(n):
        a, b = map(float, input().split())
        amount += int(a)
        gpa += a * b
    print(amount, round(gpa / amount, 1))