from collections import deque

def solution(n, wires):
    
    def bfs(start, exception, n, graph):
        
        
        deq = deque()
        visited = [False] * (n + 1)
        visited[start] = True
        visited[exception] = True
        deq.append(start)
        
        cnt = 1
        
        while deq:
            n = deq.popleft()
            
            for j in graph[n]:
                if visited[j] == False:
                    deq.append(j)
                    visited[j] = True
                    cnt += 1
        return cnt 
        
        
    
    answer = float('inf')
    
    graph = [[] for _ in range(n + 1)]
    
    # check = [0] * n
    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    # print(graph)
    
    for t in range(1, n + 1):
        for q in range(1, n + 1):
            if t != q:
                tmp = bfs(t, q, n, graph)
                if abs((n - tmp) - tmp) < answer:
                    answer = abs((n - tmp) - tmp)
    
    return answer
