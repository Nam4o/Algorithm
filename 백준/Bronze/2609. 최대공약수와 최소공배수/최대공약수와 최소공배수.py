N1, N2 = map(int, input().split())

a = []

for i in range(1, N1 + 1):
    if N1 % i == 0 and N2 % i == 0:
        a.append(i)

print(max(a))
t = 1
while True:
    if (N1 * t) % N2 == 0:
        print(N1 * t)
        break
    t += 1
