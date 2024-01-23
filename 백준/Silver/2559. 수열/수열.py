import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))


mx = -float('inf')

sum = 0

for i in range(n):
    if i < k:
        sum += arr[i]
        if i == k - 1:
            if sum > mx:
                mx = sum
    else:
        sum -= arr[i - k]
        sum += arr[i]
        if sum > mx:
            mx = sum
print(mx)