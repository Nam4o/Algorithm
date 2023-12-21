S = input()

arr = [0] * 26

for i in S:
    arr[ord(i) - 97] += 1
print(*arr)