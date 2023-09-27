import heapq, sys
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    number = int(input())
    heapq.heappush(heap, number)

ans = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans += a + b
    heapq.heappush(heap, a + b)

print(ans)
