arr = list(map(int, input().split()))

num_sum = 0

for i in arr:
    num_sum += i ** 2

print(num_sum % 10)