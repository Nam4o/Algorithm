N, M = map(int, input().split())

base_list = []

for i in range(1, N+1):
    base_list.append(i)
    

for i in range(M):
    a, b = map(int, input().split())
    if a == b:
        continue
    else:
        insert_a = base_list.pop(a-1)
        insert_b = base_list.pop(b-2)

        base_list.insert(a-1, insert_b)
        base_list.insert(b-1, insert_a)


for i in range(len(base_list)):
    print(base_list[i], end=' ')