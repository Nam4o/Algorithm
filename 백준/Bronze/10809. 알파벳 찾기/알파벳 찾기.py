S = str(input())
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = []
for i in alpha:
    if i in S:
        for t in range(len(S)):
        
            if i in result:
                continue
            else:
                if i == S[t]:
                    result.append(t)           
                    break 
    else: 
        result.append(-1)

for i in range(len(result)):
    print(result[i], end=' ')