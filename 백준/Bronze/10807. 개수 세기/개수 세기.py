number = int(input())

num_list = list(map(int, input().split()))
want_find = int(input())
result = 0
for i in range(number):
    if num_list[i] == want_find:
        result += 1
    else:
        continue
print(result)
    