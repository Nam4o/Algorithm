tc = int(input())
for i in range(tc):
    N = int(input())
    front_list  = []
    num_list = [1, 1, 1, 2, 2]

    for i in range(N):
        if N <= 5:
            if N <= 3:
                front_list.append(1)
            else:
                front_list.append(2)    
        

        elif N >= 6:
            num_list.append(num_list[len(num_list)-1] + num_list[len(num_list)-5])

    if N >= 6:
        print(num_list[N-1])       
    else:
        print(front_list[N-1]) 