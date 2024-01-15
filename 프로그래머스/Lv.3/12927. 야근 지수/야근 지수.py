from collections import deque

def solution(n, works):
    
    stack = deque()
    works.sort(reverse=True)
    works = deque(works)
    answer = 0
    
    for i in range(n):
        if not stack:
            if works:
                stack.append(works.popleft() - 1)
            # if stack[-1] == 0:
            #     stack.pop()
        elif stack:
            if works:
                
                if stack[0] > works[0]:
                    stack.append(stack.popleft() - 1)
                else:
                    stack.append(works.popleft() - 1)
            else:
                stack.append(stack.popleft() - 1)
                
        if stack and stack[-1] == 0:
                    stack.pop()
                
    # print(stack)
    # print(works)
    for j in stack:
        answer += j ** 2
    for k in works:
        answer += k ** 2
            
    return answer


# import heapq

# def solution(n, works):
    
#     stack = deque()
#     works.sort(reverse=True)
#     works = deque(works)
#     answer = 0
    
#     for i in range(n):
#         if not stack:
#             if works:
#                 stack.append(works.popleft() - 1)
#             # if stack[-1] == 0:
#             #     stack.pop()
#         elif stack:
#             if works:
                
#                 if stack[-1] > works[0]:
#                     stack.append(stack.popleft() - 1)
#                 else:
#                     stack.append(works.popleft() - 1)
#             else:
#                 stack.append(stack.popleft() - 1)
#         print(stack, works)
#         if stack and stack[-1] == 0:
#                     stack.pop()
                
#     # print(stack)
#     # print(works)
#     for j in stack:
#         answer += j ** 2
#     for k in works:
#         answer += k ** 2
            
#     return answer