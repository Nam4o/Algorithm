import heapq

def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N + 1)]
    
    for i in range(len(road)):
        graph[road[i][0]].append([road[i][1], road[i][2]])
        graph[road[i][1]].append([road[i][0], road[i][2]])
            
    check = dijkstra(1, N, graph)
    
    for j in range(1, N + 1):
        if check[j] <= K:
            answer += 1
    

    return answer



def dijkstra(start, N, graph):
    heap = [(0, start)]
    times = [float('inf')] * (N + 1)
    times[start] = 0
    
    
    while heap:
        current, node = heapq.heappop(heap)
        
        for next, t in graph[node]:
            new_t = current + t
            if new_t < times[next]:
                times[next] = new_t
                heapq.heappush(heap, (new_t, next))
                
    return times
    
    
    