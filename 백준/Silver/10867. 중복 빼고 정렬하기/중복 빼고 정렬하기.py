N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()
new_list = []
for i in range(N):
    if numbers[i] in new_list:
        continue
    else:
        new_list.append(numbers[i])

for i in range(len(new_list)):
    print(new_list[i], end=' ')

