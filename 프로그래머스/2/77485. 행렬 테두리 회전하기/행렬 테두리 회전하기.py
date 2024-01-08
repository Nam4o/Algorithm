import pprint
def solution(rows, columns, queries):
    arr = [[0] * columns for _ in range(rows)]
    
    r, c = 0, 0
    for number in range(1, rows * columns + 1):
        if c == columns:
            r += 1
            c = 0
        arr[r][c] = number
        c += 1
    answer = []
    # query[0] : x1, query[1] : y1, query[2] : x2, query[3]: y2
    
    for query in queries:
        mx = float('inf')
        
        r, c = query[0] - 1, query[1] - 1
        
        for i in range(query[3] - 1, query[1] - 1, -1):
            arr[r][i], arr[r][i - 1] = arr[r][i - 1], arr[r][i]
            if arr[r][i] < mx:
                mx = arr[r][i]
            if arr[r][i - 1] < mx:
                mx = arr[r][i - 1]
        for j in range(query[0] - 1, query[2] - 1):
            arr[j][c], arr[j + 1][c] = arr[j + 1][c], arr[j][c]
            if arr[j][c] < mx:
                mx = arr[j][c]
            if arr[j + 1][c] < mx:
                mx = arr[j + 1][c]
        r, c = query[2] - 1, query[3] - 1
        for i in range(query[1] - 1, query[3] - 1):
            arr[r][i], arr[r][i + 1] = arr[r][i + 1], arr[r][i]
            if arr[r][i] < mx:
                mx = arr[r][i]
            if arr[r][i + 1] < mx:
                mx = arr[r][i + 1]
        for j in range(query[2] - 1, query[0], -1):
            arr[j][c], arr[j - 1][c] = arr[j - 1][c], arr[j][c]
            if arr[j][c] < mx:
                mx = arr[j][c]
            if arr[j - 1][c] < mx:
                mx = arr[j - 1][c]
        answer.append(mx)
        # print(arr[r][i], arr[r][i - 1])
        # pprint.pprint(arr)
        
#         mn = float('inf')
#         for i in range(query[2] - query[0]):
#             for j in range(query[3] - query[1]):
#                 if i == query[0] - 1 or i == query[2] - 1:
#                     if 
                    
            
    return answer