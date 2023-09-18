N = int(input())

for i in range(1, N + 1):
    print('*' * i + ' ' * (N - i) * 2 + '*' * i)
for j in range(1, N):
    print('*' * (N - j) + ' ' * j * 2 + '*' * (N - j))