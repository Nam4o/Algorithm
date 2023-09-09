import sys
input = sys.stdin.readline

N = int(input().strip())

positive = []
negative = []
zero = []

for _ in range(N):
    num = int(input().strip())
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

positive.sort()
negative.sort()

posi_sum = 0
nega_sum = 0

if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        if positive[i] == 1:
            posi_sum += positive[i + 1] + 1
        else:
            posi_sum += (positive[i] * positive[i + 1])
else:
    posi_sum += positive.pop(0)
    if len(positive) >= 2:
        for j in range(0, len(positive), 2):
            if positive[j] == 1:
                posi_sum += positive[j + 1] + 1
            else:
                posi_sum += (positive[j] * positive[j + 1])

if len(negative) % 2 == 0:
    for x in range(0, len(negative), 2):
        nega_sum += (negative[x] * negative[x + 1])
else:
    nega_sum += negative.pop()
    if zero and nega_sum != 0:
        nega_sum = 0
    if len(negative) >= 2:
        for y in range(0, len(negative), 2):
            nega_sum += (negative[y] * negative[y + 1])

print(posi_sum + nega_sum)