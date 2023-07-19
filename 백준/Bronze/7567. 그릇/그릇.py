stack = str(input())
list_stack = list(map(str, stack))

height = 10
i = 0
for i in range(1, len(list_stack)):
    if list_stack[i] == list_stack[i-1]:
        height += 5
    elif list_stack[i] != list_stack[i-1]:
        height += 10
    i += 1

print(height)
