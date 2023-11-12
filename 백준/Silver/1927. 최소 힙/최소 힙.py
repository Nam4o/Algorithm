import heapq, sys
input = sys.stdin.readline

heap = []
N = int(input())
for i in range(N):
    a = int(input())
    if a == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(a)
    else:
        heapq.heappush(heap, a)
