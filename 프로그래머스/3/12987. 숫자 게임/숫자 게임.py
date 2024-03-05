from collections import deque
def solution(A, B):
    answer = -1
    A.sort(reverse = True)
    A = deque(A)
    B.sort(reverse = True)
    B = deque(B)
    cnt = 0
    while B:
        if A[0] < B[0]:
            B.popleft()
            A.popleft()
            cnt += 1
        else:
            B.pop()
            A.popleft()
    # while B:
    #     if A[0] >= B[idx]:
    #         B.pop(idx)
    #         A.popleft()
    #         idx = 0
    #     else:
    #         cnt += 1
    #         B.pop(idx)
    #         A.popleft()
    #         idx = 0
            

    return cnt