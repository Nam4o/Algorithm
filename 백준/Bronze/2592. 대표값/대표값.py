dict = {}
amount = 0
for i in range(10):
    a = int(input())
    amount += a
    if a not in dict:
        dict[a] = 1
    else:
        dict[a] += 1

print(amount // 10)

for j in dict:
    if dict[j] == max(dict.values()):
        print(j)
        break