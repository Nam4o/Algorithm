N, M = map(int, input().split())


my_list = []


for i in range(1, N + 1):
    my_list.append(i)
    
for i in range(M):
    a, b = map(int, input().split())
    new_list = []
    for i in range(b-a+1):
        t = my_list.pop(a-1)
        new_list.append(t)
    new_list.reverse()
    for i in range(len(new_list)):
        my_list.insert(a-1, new_list[len(new_list)-i-1])
    
for i in range(len(my_list)):
    print(my_list[i], end=' ')
