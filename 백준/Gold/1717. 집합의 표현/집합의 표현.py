N, M = map(int, input().split())

parents = [i for i in range(N+1)]

for j in range(M):
    A, B, C = map(int, input().split())
    if A == 0:  
        i = parents[B]
        j = parents[C]
        while parents[B] != B:  
            parents[B] = parents[parents[B]] 
            B = parents[B]
        while parents[C] != C: 
            parents[C] = parents[parents[C]]
            C = parents[C]
        if B > C:
            parents[B] = C
        elif B < C:
            parents[C] = B
    else:  # A == 1:
        while parents[B] != B: 
            parents[B] = parents[parents[B]] 
            B = parents[B]
        while parents[C] != C:  
            parents[C] = parents[parents[C]]
            C = parents[C]
        if B == C:
            print('YES')
        else:
            print('NO')