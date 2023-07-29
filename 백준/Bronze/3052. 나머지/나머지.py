my_list = []

new_list = []

for i in range(10):
    number = int(input())
    my_list.append(number)

for i in range(len(my_list)):
    left = my_list[i] % 42
    if left not in new_list: 
        new_list.append(left)
        
print(len(new_list))