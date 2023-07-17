N = int(input())

i = 2
for i in range(2, N+1):
    if N % i == 0:
        while i <= N+1:
            if N % i == 0:
                print(i)
                N /= i
            else:
                i += 1
    else:
        pass
    i += 1