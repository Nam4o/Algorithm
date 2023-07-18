N = int(input())
i = 1
list_N = []
for i in range(1, N + 1):
    numbers = int(input())
    list_N.append(numbers)
    i += 1
list_N.sort()

check = 0
for check in range(0, N): 
    print(list_N[check])
    check += 1