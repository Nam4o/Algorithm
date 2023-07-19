A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


D = []
if A[0] == B[0]:
    D.append(C[0])
    if B[1] == C[1]:
        D.append(A[1])
    elif A[1] == B[1]:
        D.append(C[1])
    elif A[1] == C[1]:
        D.append(B[1])
elif A[0] == C[0]:
    D.append(B[0])
    if B[1] == C[1]:
        D.append(A[1])
    elif A[1] == B[1]:
        D.append(C[1])
    elif A[1] == C[1]:
        D.append(B[1])
elif B[0] == C[0]:
    D.append(A[0])
    if B[1] == C[1]:
        D.append(A[1])
    elif A[1] == B[1]:
        D.append(C[1])
    elif A[1] == C[1]:
        D.append(B[1])
        
print(D[0], D[1])
    