N, K = map(int, input().split())

n_fac = 1
k_fac = 1
f_fac = 1

for i in range(1, N + 1):
    n_fac *= i

for j in range(1, K + 1):
    k_fac *= j

for k in range(1, (N - K) + 1):
    f_fac *= k

print((n_fac) // (f_fac * k_fac))
