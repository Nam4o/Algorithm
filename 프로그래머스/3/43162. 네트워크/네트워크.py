def solution(n, arr):
    parents = [_ for _ in range(n)]
    def find_set(x):
        if x == parents[x]:
            return x
        else:
            parents[x] = find_set(parents[x])
            return parents[x]

    def union(x, y):
        px, py = find_set(x), find_set(y)
        if px != py:
            if px < py:
                parents[px] = py
            else:
                parents[py] = px


    # arr = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i != j and arr[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    # graph = [[1], [0], []]
    for i in range(n):
        if graph[i]:
            for j in graph[i]:
                if find_set(i) != find_set(j):
                    union(i, j)
    for i in range(n):
        parents[i] = find_set(i)

    answer = len(set(parents))
    return answer