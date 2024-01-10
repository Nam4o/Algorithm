arr = list(map(int, input().split()))

mn = float('inf')
for i in range(5):
    for j in range(5):
        for k in range(5):
            if i != j and i != k and j != k:
                t = min(arr[i], arr[j], arr[j])
                while t % arr[i] != 0 or t % arr[j] != 0 or t % arr[k] != 0:
                    t += 1
                if t < mn:
                    mn = t

print(mn)