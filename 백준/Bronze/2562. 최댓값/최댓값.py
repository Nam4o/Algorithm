result = []
my_dict = {}
for i in range(1, 10):
    number = int(input())
    result.append(number)
    my_dict[i] = number

print(max(result))
print([x for x, v in my_dict.items() if v== max(result)][0])