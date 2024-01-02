import sys, heapq
input = sys.stdin.readline

n = int(input())

arr = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))

sne = []

heapq.heappush(sne, arr[0][1])

for i in range(1, len(arr)):
    if sne[0] > arr[i][0]:


        heapq.heappush(sne, arr[i][1])
    else:
        heapq.heappop(sne)
        heapq.heappush(sne, arr[i][1])

print(len(sne))