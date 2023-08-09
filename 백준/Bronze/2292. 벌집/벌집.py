N = int(input())
i = 0
j = 6
k = 1
while j * i + 1 <= 10**9:
    if N == 1:
        print(1)
        break
    elif 1 + (j * (i)) < N <= 1 + (j * ((i + k))):
        print(k + 1)
        break
    else:
        i += k
        k += 1
