def fibo2(n):
		f = [0] * (n + 1)
		f[0] = 0
		f[1] = 1
		for i in range(2, n + 1):
				f[i] = f[i - 1] + f[i - 2]

		return f[n]

N = int(input())

result = 1
for i in range(1,N + 1):
    if i - 1 == 0:
        continue
    else:
        result += fibo2(i- 1)

print(result % 10007)