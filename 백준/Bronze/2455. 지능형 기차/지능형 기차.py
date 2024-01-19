amount = 0
mx = 0
for i in range(4):
    a, b = map(int, input().split())
    amount += b - a
    if amount > mx:
        mx = amount

print(mx)