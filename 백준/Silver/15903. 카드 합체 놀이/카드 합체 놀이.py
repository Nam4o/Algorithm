import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr = deque(arr)

heap = []
for i in range(M):
    if heap:
        if arr:
            if heap[0] < arr[0]:
                a = heappop(heap)
                if heap:
                    if heap[0] < arr[0]:
                        b = heappop(heap)
                    else:
                        b = arr.popleft()
                else:
                    b = heappop(heap)
            else:
                a = arr.popleft()
                if arr:
                    if heap[0] < arr[0]:
                        b = heappop(heap)
                    else:
                        b = arr.popleft()
                else:
                    b = heappop(heap)
        else:
            a = heappop(heap)
            b = heappop(heap)
    else:
        a = arr.popleft()
        b = arr.popleft()
    c = a + b
    heappush(heap, c)
    heappush(heap, c)

print(sum(arr) + sum(heap))