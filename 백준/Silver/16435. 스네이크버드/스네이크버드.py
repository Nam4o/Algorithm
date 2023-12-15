N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

for i in arr:
    if i <= L:
        L += 1
    else:
        break
print(L)