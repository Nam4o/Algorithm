import heapq, sys
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    heapq.heappush(heap, -(int(input())))
for i in range(N):
    print(-(heapq.heappop(heap)))