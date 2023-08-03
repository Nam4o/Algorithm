A, B = map(str, input().split())

def reverseNum(x):
    new_x = []
    for i in range(1, len(x) + 1):
        new_x.append(x[-i])
    new_number = ''
    for j in range(len(new_x)):
        new_number += new_x[j]
        
    return int(new_number)     

if reverseNum(A) > reverseNum(B):
    print(reverseNum(A))
else:
    print(reverseNum(B))
