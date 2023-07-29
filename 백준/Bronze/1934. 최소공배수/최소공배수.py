tc = int(input())

for i in range(tc):
    A, B = map(int, input().split())
    a_list = []
    b_list = []
    for i in range(1, 45001):
        if A % i == 0 and B % i == 0:
            a_list.append(i)
        else:
            continue
    print((A*B)//(max(a_list)))
        